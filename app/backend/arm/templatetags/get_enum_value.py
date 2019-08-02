from django import template
from Industry import DURATION_MINS, FREQUENCY_MULTIPLE, DURATION

import logging
logger = logging.getLogger( __file__ )

register = template.Library()
#
#  example template call {{ X|get_enum_value:"DURATION,MIN2T5" }}
#
@register.filter(name='get_enum_value')
def get_enum_value( value, args ):
    if args is None:
        return False
    #arg_list = [arg.strip() for arg in args.split(',')]
    logging.debug( "[ TEMPLATE TAG ARGS ]: %s , %s" % ( value, args )  )

    # arg[0] is enum to target
    enum = args
    #value = arg_list[1]

    if enum == 'DURATION':
        return DURATION.get_value( value )
    elif enum == 'DURATION_MINS':
        return DURATION_MINS.get_value( value )
    elif enum == 'FREQUENCY_MULTIPLE':
        return FREQUENCY_MULTIPLE.get_value( value )
    else:
        return False
