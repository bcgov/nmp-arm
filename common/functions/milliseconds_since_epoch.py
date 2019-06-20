import datetime
from django.utils.timezone import utc

def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0).replace( tzinfo=utc )
    delta = dt - epoch
    # total_seconds() in python 2.7
    return ( (delta.microseconds + (delta.seconds + delta.days * 24 * 3600) * 10**6) / 10**6  )

def unix_time_millis(dt):
    return int( unix_time(dt) * 1000.0 )
