from ztag.transform import ZMapTransform, ZMapTransformOutput
from ztag import protocols, errors
from ztag.transform import Transformable
import re

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import http

class CWMPTransform(http.HTTPTransform):

    name = "cwmp/generic"
    port = None
    protocol = protocols.CWMP
    subprotocol = protocols.CWMP.GET

