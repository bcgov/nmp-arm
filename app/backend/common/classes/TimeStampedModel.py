#
# Code taken with permission from Carl Meyer's
# very useful django-model-utils
#
from django.db import models
import datetime
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _

#from south.modelsinspector import add_introspection_rules
#add_introspection_rules([], ["^common\.abstract_classes\.timestamped_model\.AutoCreatedField"])
#add_introspection_rules([], ["^common\.abstract_classes\.timestamped_model\.AutoLastModifiedField"])

def utcnow():
    return datetime.datetime.utcnow().replace(tzinfo=utc)

class AutoCreatedField(models.DateTimeField):

    """
    A DateTimeField that automatically populates itself at
    object creation.
    By default, sets editable=False, default=now
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', utcnow)
        super(AutoCreatedField, self).__init__(*args, **kwargs)


class AutoLastModifiedField(AutoCreatedField):
    """
    A DateTimeField that updates itself on each save() of
    the model.
    By default, sets editable=False and default=now.
    """
    def pre_save(self, model_instance, add):
        value = utcnow()
        setattr(model_instance, self.attname, value)
        return value

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.

    --------------------------------------------
    example usage:
    --------------------------------------------
    from model_utils import TimeStampedModel

    class Flavor(TimeStampedModel):
        title = models.CharField(max_length=200)

    """
    date_created = AutoCreatedField(_('created'))
    date_updated = AutoLastModifiedField(_('modified'))
    class Meta:
        abstract = True

