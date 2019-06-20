#
#  django imports
#
from django.conf import settings
#
#  sys imports
#
from Crypto.Cipher import AES
import base64
# import logging
# logger = logging.getLogger( __file__ )


class AESWrapper(object):
    ''' based on:
    http://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
    '''
    
    bs = 32

    def __init__(self, passphrase=None, salt=None, *args, **kargs):
        if not passphrase:
            passphrase = settings.PASSPHRASE
            
        if len( passphrase ) >= self.bs:
            self.passphrase = passphrase[:self.bs]
        else:
            self.passphrase = self._pad( passphrase )
                        
        if not salt:
            salt = settings.PASSPHRASE_SALT
        self.salt = salt
        
        if len( salt ) >= self.salt:
            self.salt = salt[:AES.block_size]
        else:
            self.salt = self._pad_block_size( self.salt )
        
    def encrypt(self, raw):
        raw = self._pad( raw )
        cipher = AES.new( self.passphrase, AES.MODE_ECB, self.salt )
        return base64.b64encode( self.salt + cipher.encrypt(raw) )

    def decrypt(self, enc):
        enc = base64.b64decode( enc )
        cipher = AES.new( self.passphrase, AES.MODE_ECB, self.salt )
        return self._unpad( cipher.decrypt( enc[ AES.block_size:] ) )

    def _pad(self, s):
        return s + ( self.bs - len(s) % self.bs ) * chr( self.bs - len(s) % self.bs ) 

    def _unpad(self, s):
        return s[0:-ord(s[-1])]

    def _pad_block_size(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
