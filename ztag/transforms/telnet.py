import json

from ztag import protocols, errors
from ztag.transform import *

class TelnetTransform(ZGrabTransform):

    name = "telnet/banner"

    port = None
    protocol = protocols.TELNET
    subprotocol = protocols.TELNET.BANNER

    def _transform_object(self, obj):
        scan_id = list(obj["data"].keys())[0]

        #print(">>>>> HTTPTransform _transform_object")
        zout = super(TelnetTransform, self)._transform_object(obj)
        results = self.get_scan_results(obj)
        if not results:
            return zout
        #print(json.dumps(obj,indent=2,default=str))
        #print(json.dumps(results,indent=2,default=str))
        #obj = results

        if "error" in obj:
            raise errors.IgnoreObject("Error")

        data = Transformable(obj)
        out = dict()
        out["support"] = True

        #t = data['data']['telnet']
        t = results
        #print(json.dumps(t, indent=2))
        #banner = t['banner'].resolve()
        banner = t['banner']
        #print(banner)
        if banner:
            out['banner'] = self.clean_banner(banner)
        #will = t['will'].resolve()
        try :
            will = t['will']
            if will:
                out['will'] = will
        #wont = t['wont'].resolve()
        except :
            out['will'] = ""

        try :
            wont = t['wont']
            if wont:
                out['wont'] = wont
        except :
            out['wont'] = ""

        try :
            do = t['do'].resolve()
            if do:
                out['do'] = do
        except :
            out['do'] = ""

        try :
            #dont = t['dont'].resolve()
            dont = t['dont']
            if dont:
                out['dont'] = dont
        except :
            out['dont'] = ""

        if not out:
            raise errors.IgnoreObject("Empty output dict")

        out['ip_address'] = obj['ip']
        out['timestamp'] = obj['data'][scan_id]['timestamp']
        zout = ZMapTransformOutput()
        zout.transformed = out
        return zout
