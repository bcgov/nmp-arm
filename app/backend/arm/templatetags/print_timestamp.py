from django import template
from django.utils.timezone import utc
import datetime
register = template.Library()

import logging
logger = logging.getLogger( __file__ )

def print_timestamp(timestamp):
    try:
        #assume, that timestamp is given in seconds with decimal point
        ts = float(timestamp)
    except ValueError:
        return None
    
    logger.debug( "timestamp to convert = %s" % timestamp )
    # make sure we divide by 1000 for seconds
    return datetime.datetime.fromtimestamp(ts/1000.0, tz=utc)
    #return return_date.replace(tzinfo=utc)

register.filter(print_timestamp)
