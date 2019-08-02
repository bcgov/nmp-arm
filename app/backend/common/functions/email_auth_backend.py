from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
import logging

logger = logging.getLogger( __file__ )

class EmailAuthBackend(ModelBackend):
    """
    Email Authentication Backend

    Allows a user to sign in using an email/password pair rather than
    a email/password pair.
    """
    supports_inactive_user = False
    #supports_object_permissions=False
    #supports_anonymous_user=False
    
    def authenticate(self, email=None, password=None):
        logger.debug( "Email: %s" % email )
        #logger.debug( "Password: %s" % password )
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return AnonymousUser()