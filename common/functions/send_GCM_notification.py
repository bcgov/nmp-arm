#
#  django imports
#
from django.conf import settings

#
#  sys imports
#
from gcm import GCM
from gcm.gcm import GCMNotRegisteredException, GCMUnavailableException, GCMMismatchSenderIdException
import logging
logger = logging.getLogger( __file__ )

#
#  local imports
#
from common.functions.log_traceback import LogTraceback

def send_GCM_notification( token, data ):

    logger.debug( "Sending GCM Notification to [%s]..." % token )

    try:

        gcm = GCM( settings.GCM_API_KEY )
        
        # Plaintext request
        #response = gcm.plaintext_request( registration_id=token, collapse_key='Updated Steps', data=data, time_to_live=86400 ) <-- currently broken in library
        response = gcm.plaintext_request( registration_id=token, data=data )
    
        logger.debug( "Sent Push to: [%s] sent: %s" % ( token, response ) )
        return "Success"
        
    except GCMNotRegisteredException:
        logger.error( "Token [%s] Not Registered!" % token )
        return "NotRegistered"
    
    except GCMMismatchSenderIdException:
        logger.error( "Token [%s] Bad Sender error" % token )
        return "Mismatch"
    
    except GCMUnavailableException:
        logger.error( "Failed for [%s]... try again" % token )
        return "Unavailable"
    
    except:
        LogTraceback()
        return "Error"