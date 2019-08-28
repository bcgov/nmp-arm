from copy import deepcopy
from base64 import b64encode, b64decode
from zlib import compress, decompress
try:
    from pickle import loads, dumps
except ImportError:
    from pickle import loads, dumps

from django.db import models
from django.utils.encoding import force_unicode

# for JSON addition
from django import forms
from django.forms import widgets
from django.forms.util import flatatt, ValidationError
from django.utils import simplejson
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

import logging
logger = logging.getLogger( __file__ )

# see http://djangosnippets.org/snippets/1694/
class PickledObject(str):
    """
    A subclass of string so it can be told whether a string is a pickled
    object or not (if the object is an instance of this class then it must
    [well, should] be a pickled one).

    Only really useful for passing pre-encoded values to ``default``
    with ``dbsafe_encode``, not that doing so is necessary. If you
    remove PickledObject and its references, you won't be able to pass
    in pre-encoded values anymore, but you can always just pass in the
    python objects themselves.

    """
    pass

def dbsafe_encode(value, compress_object=False):
    """
    We use deepcopy() here to avoid a problem with cPickle, where dumps
    can generate different character streams for same lookup value if
    they are referenced differently.

    The reason this is important is because we do all of our lookups as
    simple string matches, thus the character streams must be the same
    for the lookups to work properly. See tests.py for more information.
    """
    if not compress_object:
        value = b64encode(dumps(deepcopy(value)))
    else:
        value = b64encode(compress(dumps(deepcopy(value))))
    return PickledObject(value)

def dbsafe_decode(value, compress_object=False):
    if not compress_object:
        value = loads(b64decode(value))
    else:
        value = loads(decompress(b64decode(value)))
    return value


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^common\.functions\.PickledObject\.PickledObjectField"])

class PickledObjectField(models.Field, metaclass=models.SubfieldBase):
    """
    A field that will accept *any* python object and store it in the
    database. PickledObjectField will optionally compress it's values if
    declared with the keyword argument ``compress=True``.

    Does not actually encode and compress ``None`` objects (although you
    can still do lookups using None). This way, it is still possible to
    use the ``isnull`` lookup type correctly. Because of this, the field
    defaults to ``null=True``, as otherwise it wouldn't be able to store
    None values since they aren't pickled and encoded.

    """

    def __init__(self, *args, **kwargs):
        self.compress = kwargs.pop('compress', False)
        self.protocol = kwargs.pop('protocol', 2)
        kwargs.setdefault('null', True)
        kwargs.setdefault('editable', True)
        super(PickledObjectField, self).__init__(*args, **kwargs)

    def get_default(self):
        """
        Returns the default value for this field.

        The default implementation on models.Field calls force_unicode
        on the default, which means you can't set arbitrary Python
        objects as the default. To fix this, we just return the value
        without calling force_unicode on it. Note that if you set a
        callable as a default, the field will still call it. It will
        *not* try to pickle and encode it.

        """
        if self.has_default():
            if callable(self.default):
                return self.default()
            return self.default
        # If the field doesn't have a default, then we punt to models.Field.
        return super(PickledObjectField, self).get_default()

    def to_python(self, value):
        """
        B64decode and unpickle the object, optionally decompressing it.

        If an error is raised in de-pickling and we're sure the value is
        a definite pickle, the error is allowed to propogate. If we
        aren't sure if the value is a pickle or not, then we catch the
        error and return the original value instead.

        """
        if value is not None:
            try:
                value = dbsafe_decode(value, self.compress)
            except:
                # If the value is a definite pickle; and an error is raised in
                # de-pickling it should be allowed to propogate.
                if isinstance(value, PickledObject):
                    raise
        return value

    def get_prep_value(self, value):
        """
        Pickle and b64encode the object, optionally compressing it.

        The pickling protocol is specified explicitly (by default 2),
        rather than as -1 or HIGHEST_PROTOCOL, because we don't want the
        protocol to change over time. If it did, ``exact`` and ``in``
        lookups would likely fail, since pickle would now be generating
        a different string.

        """
        if value is not None and not isinstance(value, PickledObject):
            # We call force_unicode here explicitly, so that the encoded string
            # isn't rejected by the postgresql_psycopg2 backend. Alternatively,
            # we could have just registered PickledObject with the psycopg
            # marshaller (telling it to store it like it would a string), but
            # since both of these methods result in the same value being stored,
            # doing things this way is much easier.
            value = force_unicode(dbsafe_encode(value, self.compress))
        return value

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    def get_internal_type(self):
        return 'TextField'

    def get_prep_lookup(self, lookup_type, value):
        if lookup_type not in ['exact', 'isnull']:
            raise TypeError('Lookup type %s is not supported.' % lookup_type)
        return self.get_prep_value(value)

    def formfield(self, **kwargs):
        defaults = {'form_class': JSONField }
        defaults.update(kwargs)
        return super(PickledObjectField, self).formfield(**defaults)

# South support; see http://south.aeracode.org/docs/tutorial/part4.html#simple-inheritance
try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    pass
else:
    add_introspection_rules([], [r"^picklefield\.fields\.PickledObjectField"])

class JSONWidget (widgets.Widget):

    def __init__(self, attrs=None):
        self.attrs = {'cols': '84', 'rows': '5'}
        if attrs:
            self.attrs.update(attrs)

    def render(self, name, value, attrs=None):
        if not isinstance(value, str):
            value = simplejson.dumps(value)

        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(
                '<textarea%s>%s</textarea>' %
                    ( flatatt(final_attrs), conditional_escape(force_unicode(value)) )
            )

    def value_from_datadict(self, data, files, name):
        return data.get(name, '{ }')

class JSONField (forms.Field):

    widget = JSONWidget

    default_error_messages = {
        'invalid': 'Enter a valid JSON string.'
    }

    def __init__(self, max_value=None, min_value=None, *args, **kwargs):
        super(JSONField, self).__init__(*args, **kwargs)

    def prepare_value(self, value):
        raw = "%s" % value
        return raw.replace( "u'", "'" ).replace( "'", '"' )

    def clean (self, value):
        super(JSONField, self).clean(value)
        if value is None or value == '':
            return { }
        try:
            value = simplejson.loads(value)
        except ValueError:
            raise ValidationError( self.error_messages['invalid'] )
        return value
