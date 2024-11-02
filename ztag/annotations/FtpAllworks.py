import re
from ztag.annotation import Annotation
from ztag.annotation import OperatingSystem
from ztag.annotation import Type
from ztag.annotation import Manufacturer
from ztag import protocols
import ztag.test


class FtpAllworks(Annotation):
    protocol = protocols.FTP
    subprotocol = protocols.FTP.BANNER
    port = None

    manufact_re = re.compile(
                        "^220 Allworx FTP server ready",
                        re.IGNORECASE
                        )

    tests = {
        "FtpAllworks_1": {
            "global_metadata": {
                "device_type": Type.VOIP,
                "manufacturer": Manufacturer.ALLWORKS,
            }
        }
    }

    def process(self, obj, meta):
        banner = obj["banner"]
        tagged = False

        if self.manufact_re.search(banner):
            meta.global_metadata.device_type = Type.VOIP
            meta.global_metadata.manufacturer = Manufacturer.ALLWORKS
            tagged = True

        if tagged:
            return meta
        else:
            return None

    """ Tests
    "220 Allworx FTP server ready\r\n"
    "220 Allworx FTP server ready\r\n"
    "220 Allworx FTP server ready\r\n"
    "220 Allworx FTP server ready\r\n"
    "220 Allworx FTP server ready\r\n"
    """
