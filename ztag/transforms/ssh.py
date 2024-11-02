import json

from datetime import datetime

from ztag.transform import ZGrabTransform, ZMapTransformOutput, Transformable
from ztag import errors, protocols

def set_value(dict, key, value):
    """Set the given value for the given key in the given dictionary, iff the
    value is not None and has a non-zero len (for objects with a length).
    """
    if value is None:
        return
    if hasattr(value, '__len__') and len(value) == 0:
        return

    dict[key] = value

def rename_key(dict, old_key, new_key):
    """Moves a value from old_key to new_key in the given dictionary.

    No-op if old_key doesn't exist in the dictionary."""
    try:
        dict[new_key] = dict[old_key]
        del dict[old_key]
    except KeyError:
        pass

def del_key(dict, key):
    """Deletes the given key from the given dictionary.

    No-op if key doesn't exist in the dictionary."""
    try:
        del dict[key]
    except KeyError:
        pass

def rewrite_known(dict):
    known = dict.get('known')
    if known is not None:
        for key in known.keys():
            dict[key] = True
        del dict['known']
    return dict

class SSHV2Transform(ZGrabTransform):
    """Transforms ZGrab XSSH grabs for Censys."""

    name = "ssh/v2"
    port = None
    protocol = protocols.SSH
    subprotocol = protocols.SSH.V2

    def __init__(self, *args, **kwargs):
        super(SSHV2Transform, self).__init__(*args, **kwargs)

    def _transform_object(self, obj):
        scan_id = list(obj["data"].keys())[0]

        zout = super(SSHV2Transform, self)._transform_object(obj)
        results = self.get_scan_results(obj)
        if not results:
            return zout
        #print(json.dumps(obj,indent=2,default=str))
        #print(json.dumps(results,indent=2,default=str))
        obj = results

        grab = Transformable(obj)
        #print(grab)
        #grab = grab['data']['xssh']
        #print(grab)
        out = dict()

        # banner:
        set_value(out, 'banner', grab['server_id'].resolve())

        # support:
        support = dict()
        set_value(support, 'kex_algorithms', grab['server_key_exchange']['kex_algorithms'].resolve())
        set_value(support, 'host_key_algorithms', grab['server_key_exchange']['host_key_algorithms'].resolve())
        set_value(support, 'first_kex_follows', grab['server_key_exchange']['first_kex_follows'].resolve())

        client_to_server = dict()
        set_value(client_to_server, 'ciphers', grab['server_key_exchange']['client_to_server_ciphers'].resolve())
        set_value(client_to_server, 'macs', grab['server_key_exchange']['client_to_server_macs'].resolve())
        set_value(client_to_server, 'compressions', grab['server_key_exchange']['client_to_server_compression'].resolve())
        set_value(client_to_server, 'languages', grab['server_key_exchange']['client_to_server_languages'].resolve())
        set_value(support, 'client_to_server', client_to_server)

        server_to_client = dict()
        set_value(server_to_client, 'ciphers', grab['server_key_exchange']['server_to_client_ciphers'].resolve())
        set_value(server_to_client, 'macs', grab['server_key_exchange']['server_to_client_macs'].resolve())
        set_value(server_to_client, 'compressions', grab['server_key_exchange']['server_to_client_compression'].resolve())
        set_value(server_to_client, 'languages', grab['server_key_exchange']['server_to_client_languages'].resolve())
        set_value(support, 'server_to_client', server_to_client)

        set_value(out, 'support', support)

        # selected:
        selected = grab['algorithm_selection'].resolve()
        if selected is not None:
            rename_key(selected, 'dh_kex_algorithm', 'kex_algorithm')
            rename_key(selected, 'client_to_server_alg_group', 'client_to_server')
            rename_key(selected, 'server_to_client_alg_group', 'server_to_client')
        set_value(out, 'selected', selected)

        # key_exchange:
        key_exchange = dict()
        set_value(key_exchange, 'ecdh_params', grab['key_exchange']['ecdh_params'].resolve())
        set_value(key_exchange, 'dh_params', grab['key_exchange']['dh_params'].resolve())
        try:
            del key_exchange['dh_params']['server_public']
        except KeyError:
            pass
        set_value(out, 'key_exchange', key_exchange)

        # server_host_key:
        host_key = dict()
        for clone_key in ['fingerprint_sha256', 'rsa_public_key', 'dsa_public_key', 'ecdsa_public_key', 'ed25519_public_key']:
            # a bunch of keys we just need to copy verbatim from the grab
            set_value(host_key, clone_key, grab['key_exchange']['server_host_key'][clone_key].resolve())
        set_value(host_key, 'key_algorithm', grab['key_exchange']['server_host_key']['algorithm'].resolve())

        certkey_public_key = grab['key_exchange']['server_host_key']['certkey_public_key'].resolve()
        if certkey_public_key is not None:
            rename_key(certkey_public_key, 'cert_type', 'type')
            # 2018/09/11: Workaround for mis-typed CertType.id field in ES; actual type is uint32,
            # current ES type is keyword (string). Added 'exclude={elasticsearch}' to the schema,
            # but to prevent attempted insertions of mistyped values, we need to actually remove the
            # id field as well.
            if 'type' in certkey_public_key:
                cert_type = certkey_public_key['type']
                del_key(cert_type, 'id')

            del_key(certkey_public_key, 'reserved')

            signature_key = certkey_public_key.get('signature_key')
            if signature_key is not None:
                del_key(signature_key, 'raw')
                rename_key(signature_key, 'algorithm', 'key_algorithm')
                certkey_public_key['signature_key'] = signature_key

            # rewrite extensions and critical_options to maps of string -> bool:
            extensions = certkey_public_key.get('extensions')
            if extensions is not None:
                certkey_public_key['extensions'] = rewrite_known(extensions)
            critical_options = certkey_public_key.get('critical_options')
            if critical_options is not None:
                certkey_public_key['critical_options'] = rewrite_known(critical_options)

            key = certkey_public_key.get('key')
            if key is not None:
                del_key(key, 'raw')
                certkey_public_key['key'] = key

            sig = certkey_public_key.get('signature')
            if sig is not None:
                formatted_sig = dict()
                parsed = sig.get('parsed')
                if parsed is not None:
                    set_value(formatted_sig, 'value', parsed.get('value'))
                    alg = dict()
                    set_value(alg, 'name', parsed.get('algorithm'))
                    set_value(formatted_sig, 'signature_algorithm', alg)
                certkey_public_key['signature'] = formatted_sig

            set_value(host_key, 'certkey_public_key', certkey_public_key)

        set_value(out, 'server_host_key', host_key)

        if len(out) == 0:
            raise errors.IgnoreObject("Empty SSH protocol output dict")

        zout = ZMapTransformOutput()
        zout.transformed = out
        return zout
