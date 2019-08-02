#
#  django imports
#

#
#  system imports
#
from urllib import urlencode
import json
import logging
import requests
logger = logging.getLogger( __file__ )

#
#  app imports
#
from common.functions.log_traceback import LogTraceback

def send_json_post( url, json_dict ):
    try:
        # convert json_dict to JSON
        json_data = json.dumps(json_dict)
    
        headers = {'content-type': 'application/json'}
    
        r = requests.post(url, data=json_data, headers=headers)
    
        if r.status_code == 200:
            return r.json()
        else:
            logger.debug( "[%s] Result was: %s" % (r.status_code, r.text ) )
            return r.json()
        
    except requests.ConnectionError, args:
        return { 'result': 'error', 'errors': "ConnectionError: %s" % args }
    
    except Exception, args:
        LogTraceback()
        logger.error( "Error: %s" % args )
        return { 'result': 'error', 'errors': "Generic: %s" % args }

def send_json_get( url, my_args=None ):

    headers = {'content-type': 'application/json'}

    if my_args:
        # convert my_args into query_string args
        encoded_args = urlencode( my_args )

        # make request
        r = requests.get('%s?%s' % ( url, encoded_args ), headers=headers )

    else:    
        # make request
        r = requests.get( url, headers=headers )

    if r.status_code == 200:
        return r.json()
    else:
        LogTraceback()
        logger.debug( "[%s] Result was: %s" % (r.status_code, r.text ) )
        return r.json()

