#
#  django imports
#

#
#  sys imports
#

import base64


class B64Wrapper(object):

    def __init__(self, *args, **kargs):
        pass

    def encrypt(self, raw):
        return base64.b64encode( raw )


    def decrypt(self, enc):
        return base64.b64decode( enc )
