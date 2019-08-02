from django import template
from django.template.defaultfilters import slugify
import logging
logger = logging.getLogger( __file__ )
register = template.Library()

#@register.filter
#def is_admin( user ):
#    if not user:
#        return False
#    #logger.debug( "User: [%s]" % user )
#    if user.is_authenticated() and user.groups.filter( name__in = [ 'Admin' ] ).exists():
#        return True
#    else:
#        return False

#@register.filter
#def is_therapist( user ):
#    #logger.debug( "User: [%s]" % user )
#    if not user:
#        return False
#    if user.is_authenticated() and user.groups.filter( name__in = [ 'Advisor', ' Admin' ] ).exists():
#        return True
#    else:
#        return False

@register.filter
def body_name( page_name ):
    return slugify( page_name )
