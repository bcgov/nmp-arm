from django.core import serializers
from django.forms.util import ErrorDict
from django.http import HttpResponse
from django.core.exceptions import ImproperlyConfigured

import logging
logger = logging.getLogger( __file__ )
import json

class JSONResponseMixin(object):
    """
    Responds with json
    """
    content_type = "application/json"

    def get_content_type(self):
        if self.content_type is None:
            raise ImproperlyConfigured(u"%(cls)s is missing a content type. "
                u"Define %(cls)s.content_type, or override "
                u"%(cls)s.get_content_type()." % {
                "cls": self.__class__.__name__
            })
        return self.content_type

    def render_json_object_response(self, objects, status=200, **kwargs):
        """
        Wraps the json serializer
        """
        try:
            if type( objects ) == ErrorDict:
                json_data = json.dumps( objects  )
            elif isinstance( objects, dict ):
                json_data = json.dumps( objects )
            elif isinstance( objects, list ):
                json_data = json.dumps( objects )
            else:
                #print type( objects )
                #print objects
                #print len( objects )
                json_data = json.dumps( objects[0] ) #TODO: Verify this!! [0]
        except Exception, e:
            logger.error( e )
            json_data = serializers.serialize( "json", objects, **kwargs )

        response = HttpResponse(json_data, content_type=self.get_content_type())
        response.status_code = status

        return response


