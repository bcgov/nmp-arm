#
#  django imports
#

#
#  sys imports
#
from Crypto import Random
from Crypto.Cipher import AES
import base64


class AESWrapper(object):
    bs = 32

    def __init__(self, passphrase, *args, **kargs):
        if len(passphrase) >= self.bs:
            self.passphrase = passphrase[:self.bs]
        else:
            self.passphrase = self._pad(passphrase)

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.passphrase, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.passphrase, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + ( self.bs - len(s) % self.bs ) * chr( self.bs - len(s) % self.bs ) 

    def _unpad(self, s):
        return s[0:-ord(s[-1])]
