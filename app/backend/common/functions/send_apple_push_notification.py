#
#  django imports
#
from django.conf import settings

#
#  sys imports
#
from APNSWrapper import APNSNotificationWrapper, APNSNotification, APNSAlert, APNSProperty
import binascii
import logging
logger = logging.getLogger( __file__ )

# 
# local imports
#
from common.functions.log_traceback import LogTraceback

def send_apple_push_notification( token, text, badge=None, sound=None, data=None ):

    logger.debug( "Sending PUSH Notification to [%s]..." % token )

    try:

        # create wrapper
        wrapper = APNSNotificationWrapper( settings.APNS_CERT, sandbox=settings.APNS_SANDBOX )

        # create message
        message = APNSNotification()
        logger.debug( "Token used: [%s]" % token )
        message.token( binascii.unhexlify( token ) )

        logger.debug( "create alert..." )
        # create custom alert message
        alert = APNSAlert()

        logger.debug( "Encoded text [%s]" % ( text.encode( "ASCII", 'ignore' ) ) )
        # add body to alert
        alert.body( text.encode( "ASCII", 'ignore' ) )

        if data:
            logger.debug( "\t\tAdding data" )

            # here is argument *arg1* with integer value *54*
            for key in data.keys():
                if isinstance( key, str ):
                    #print "Key: %s" % key
                    ekey = key.encode( "ASCII", 'ignore' )
                else:
                    ekey = "%s" % key

                #print "EKey: %s" % ekey
                #print "    : %s" % data[key]

                if isinstance( data[key], str ):
                    apns_data = APNSProperty( ekey, data[key].encode( "ASCII", 'ignore' ) )
                else:
                    apns_data = APNSProperty( ekey, data[key] )

                # append properties to notification
                #print apns_data
                message.appendProperty( apns_data )

        message.alert(alert)

        if badge:
            logger.debug( "\tBadge: [%s]" % badge )
            message.badge( badge )

        if sound:
            logger.debug( "\tSound" )
            message.sound()

        logger.debug( "\tAdding message..." )
        # add message to tuple and send it to APNS server
        wrapper.append( message )
        logger.debug( "\tSending..." )
        # On Stage the following errors for some reason
        wrapper.notify()
        logger.debug( "\tSent!" )
        
        return True

    except Exception:
        LogTraceback()
        
        return False