#
#  django imports
#
from django.db import models

#
#  sys imports
#
#import logging
#logger = logging.getLogger( __file__ )
import types

#
#  Encryption
#
from common.classes.B64Wrapper import B64Wrapper


class B64FieldException(Exception): pass

class B64FieldMixin(object):
    """

    """
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        """
        """
        self._crypter_b64 = kwargs.pop('crypter_b64', B64Wrapper)

        self._crypter = self._crypter_b64( )

        super(B64FieldMixin, self).__init__(*args, **kwargs)

    def crypter(self):
        return self._crypter

    def get_internal_type(self):
        return 'TextField'

    def to_python(self, value):
        if value is None or not isinstance(value, types.StringTypes):
            return value

        try:
            value = self.crypter().decrypt(value)
            value = value.decode('unicode_escape')
        except UnicodeEncodeError:
            pass
        except:
            pass

        return super(B64FieldMixin, self).to_python(value)

    def get_prep_value(self, value):
        if value is None or value == '':
            return value

        if isinstance(value, types.StringTypes):
            value = value.encode('unicode_escape')
            value = value.encode('ascii')
        else:
            value = str(value)
        
        encrypted_value = self.crypter().encrypt( value )
        
        value = super(B64FieldMixin, self).get_prep_value(encrypted_value)

        return encrypted_value

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)

        return value


class B64CharField(B64FieldMixin, models.CharField):
    pass


class B64TextField(B64FieldMixin, models.TextField):
    pass


class B64DateTimeField(B64FieldMixin, models.DateTimeField):
    pass


class B64IntegerField(B64FieldMixin, models.IntegerField):
    pass


class B64FloatField(B64FieldMixin, models.FloatField):
    pass


class B64EmailField(B64FieldMixin, models.EmailField):
    pass

class B64BooleanField(B64FieldMixin, models.BooleanField):
    pass


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^aes_fields\.fields\.\w+Field'])

except ImportError:
    pass