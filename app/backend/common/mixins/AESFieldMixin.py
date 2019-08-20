#
#  django imports
#
from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

#
#  sys imports
#
# import logging
# logger = logging.getLogger( __file__ )
import types

#
#  Encryption
#
from common.classes.AES_ECB_Wrapper import AESWrapper


class AESFieldException(Exception): pass

class AESFieldMixin(object, metaclass=models.SubfieldBase):
    """

    """

    def __init__(self, *args, **kwargs):
        """
        """
        self._crypter_aes = kwargs.pop('crypter_aes', AESWrapper)
        self.passphrase = kwargs.pop('passphrase', None)
        self.salt = kwargs.pop( 'salt', None )

        self.prefix = 'aesecb32$'
        if not self.passphrase:
            if hasattr(settings, 'PASSPHRASE'):
                self.passphrase = settings.PASSPHRASE
            else:
                raise ImproperlyConfigured(
                    'You must set settings.PASSPHRASE'
                )

        if not self.salt:
            if hasattr(settings, 'PASSPHRASE_SALT'):
                self.salt = settings.PASSPHRASE_SALT
            else:
                raise ImproperlyConfigured(
                    'You must set settings.PASSPHRASE_SALT'
                )

        self._crypter = self._crypter_aes( passphrase=self.passphrase, salt=self.salt )

        self.prefix = 'AESECB32#'
        # Ensure the encrypted data does not exceed the max_length
        # of the database. Data truncation is a possibility otherwise.
        self.enforce_max_length = getattr(settings, 'ENFORCE_MAX_LENGTH', False)
        if not self.enforce_max_length:
            self.enforce_max_length = kwargs.pop('enforce_max_length', False)

        super(AESFieldMixin, self).__init__(*args, **kwargs)

    def crypter(self):
        return self._crypter

    def get_internal_type(self):
        return 'TextField'

    def to_python(self, value):

        if value is None or not isinstance(value, (str,)):
            return value

        if self.prefix and value.startswith(self.prefix):
            value = value[len(self.prefix):]

            try:
                value = self.crypter().decrypt(value)
                value = value.decode('unicode_escape')
            except UnicodeEncodeError:
                pass

        return super(AESFieldMixin, self).to_python( value)

    def get_prep_value(self, value):
        value = super(AESFieldMixin, self).get_prep_value(value)
        
        if value is None or value == '':
            return value

        if isinstance(value, (str,)):
            value = value.encode('unicode_escape')
            value = value.encode('ascii')
        else:
            value = str(value)
        
        value = self.prefix + self.crypter().encrypt( value )
        
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)

        return value


class AESCharField(AESFieldMixin, models.CharField):
    pass


class AESTextField(AESFieldMixin, models.TextField):
    pass


class AESDateTimeField(AESFieldMixin, models.DateTimeField):
    pass

class AESDateField(AESFieldMixin, models.DateField):
    pass


class AESIntegerField(AESFieldMixin, models.IntegerField):
    pass


class AESFloatField(AESFieldMixin, models.FloatField):
    pass


class AESEmailField(AESFieldMixin, models.EmailField):
    pass

class AESdBooleanField(AESFieldMixin, models.BooleanField):
    pass


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^aes_fields\.fields\.\w+Field'])

except ImportError:
    pass