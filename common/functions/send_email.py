from django.core.mail import EmailMultiAlternatives
from django.template import Template, TemplateDoesNotExist
from django.template.loader import get_template
import logging
import sys

logger = logging.getLogger( __file__ )

def SendEmail( template_name, content, email_to, email_from, subject, email_bcc ):
    '''
    Send Email
     - will always send text message
     - if html version exists, it will send that also
    '''

    try:

        # handle template_name as template or path
        try:
            plaintext = get_template( '%s.txt' % template_name )
            text_content = plaintext.render( content )
        except TemplateDoesNotExist as e: # @UnusedVariable
            try:
                with open( template_name, 'r' ) as fsock:
                    plaintext = Template( fsock.read() )
                    text_content = plaintext.render( content )
            except IOError, args:
                logger.debug( 'Unable to open template_name as path or template: %s, %s' % ( Exception, args ) )
                logger.debug( 'Exception: %s' % sys.exc_info()[0] )
            except Exception:
                raise

        # create msg object and send email
        msg = EmailMultiAlternatives( subject, \
                                      text_content, \
                                      email_from, \
                                      [ email_to ])

        if email_bcc:
            msg.bcc = email_bcc

        try:
            # handle template_name as template or path
            try:
                html = get_template( '%s.html' % template_name )
                html_content = html.render( content )
            except TemplateDoesNotExist as e: # @UnusedVariable
                try:
                    with open( template_name, 'r' ) as fsock:
                        html = Template( fsock.read() )
                        html_content = html.render( content )
                except IOError, args:
                    logger.debug( 'Unable to open template_name as path or template: %s, %s' % ( Exception, args ) )
                    logger.debug( 'Exception: %s' % sys.exc_info()[0] )
                except Exception:
                    raise

            msg.attach_alternative( html_content, "text/html" )

        except Exception, args:
            logger.debug( 'HTML email failure: %s, %s' % ( Exception, args ) )
            logger.debug( 'Exception: %s' % sys.exc_info()[0] )

        msg.send()

        logging.info( '%s email sent from [%s] to [%s]' % \
                        ( template_name, email_from, email_to ) )

        return

    except Exception, args:
        logger.debug( 'Plaintext email failure: %s, %s' % ( Exception, args ) )
        logger.debug( 'Exception: %s' % sys.exc_info()[0] )

        return
