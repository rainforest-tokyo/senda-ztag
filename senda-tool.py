import os
import sys
import json
import argparse

from zsearch_definitions import protocols

from ztag.stream import Stream, Incoming, Outgoing, InputFile, OutputFile
from ztag.transform import Transform, Decoder, Encoder
from ztag.decoders import JSONDecoder
from ztag.encoders import JSONEncoder
from ztag.annotation import Annotation
from ztag.annotator import Annotator, CheckAnnotator, AnnotationTesting
from ztag.transformer import ZMapTransformer
from ztag.log import Logger
from ztag.classargs import subclass_of

from datetime import datetime

def uint16(s):
    x = int(s)
    if x < 0 or x > 65535:
        raise argparse.ArgumentTypeError
    return x

def zsearch_protocol(s):
    try:
        return protocols.Protocol.from_pretty_name(s)
    except KeyError as e:
        raise argparse.ArgumentTypeError(e)


def zsearch_subprotocol(s):
    try:
        return protocols.Subprotocol.from_pretty_name(s)
    except KeyError as e:
        raise argparse.ArgumentTypeError(e)

def do(fd, in_port, in_protocol, in_subprotocol):
    Annotation.load_annotations(False)

    metadata = dict()

    port = in_port
    protocol = zsearch_protocol(in_protocol)
    subprotocol = zsearch_subprotocol(in_subprotocol)
    scan_id = 0
    transform_kwargs = dict()
    transform_args = list()

    #z_transform = ZGrab2Transform()
    transform = ZMapTransformer.find_transform(port, protocol, subprotocol, scan_id, *transform_args, **transform_kwargs)

    incoming = InputFile(input_file=fd)
    decoder = JSONDecoder()
    encoder = JSONEncoder(port, protocol, subprotocol, scan_id)
    outgoing = OutputFile(output_file=sys.stdout, destination="full_ipv4")

    tagger = CheckAnnotator(port, protocol, subprotocol,
                       debug=False)
    num_tags = len(tagger.eligible_tags)
    metadata['eligible_tags'] = num_tags

    for obj in incoming:
        out = obj
        try :
            out = decoder.transform(out)
        except :
            continue

        out = transform.transform(out)
        out = tagger.transform(out)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='zgrab2出力ファイル')
    args = parser.parse_args()

    params = os.path.basename(args.filename).split('.')[0].split('_')
    #print(params)
    port = int(params[1])
    protocol = params[2]
    if "http" == protocol :
        subprotocols = ["get"]
    elif "telnet" == protocol :
        subprotocols = ["banner"]
    elif "ssh" == protocol :
        subprotocols = ["v2"]
    elif "https" == protocol :
        subprotocols = ["tls","get"]
    else :
        exit(1)

    for subprotocol in subprotocols :
        do(open(args.filename), port, protocol, subprotocol)

if __name__ == "__main__":
    main()

