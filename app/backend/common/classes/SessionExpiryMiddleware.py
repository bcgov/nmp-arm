#
#  django imports
#
from django.conf import settings

#
#  sys imports
#
# Logging doesn't appear to work here!!
#import logging
#logger = logging.getLogger( __file__ )

class SessionExpiryMiddleware(object):
    """ Set the session expiry according to settings """
    def process_request(self, request):
            
        if 'mobile' in request.session:
            #print( "Session Expiry: Mobile [%s]" % settings.SESSION_EXPIRY_MOBILE )
            request.session.set_expiry( settings.SESSION_EXPIRY_MOBILE )
        else:
            #print( "Session Expiry: Generic [%s]" % settings.SESSION_EXPIRY )
            request.session.set_expiry(settings.SESSION_EXPIRY)
            #request.session.modified = True
            #request.session.save()

        # remove expired sessions vi a cronjob and the following command:
        # $ python manage.py clearsessions

        return None
