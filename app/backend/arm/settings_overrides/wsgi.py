"""
Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.
"""
''' TODO: NOTE: WSGIPassAuthorization On '''

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arm.settings")
os.environ.setdefault("ENVIRONMENT", "dev" )

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()

def application( environ, start_response ):
    os.environ['ENVIRONMENT'] = environ['ENVIRONMENT']
    return _application( environ, start_response )

