import logging
import sys
import traceback
logger = logging.getLogger( 'traceback' )

def LogTraceback():
    #logger.error( "=== Exception: %s | %s" % ( exception, args ) )

    exception_type, value, tb = sys.exc_info()
    logger.error( "==== Exception: %s | %s ====" % ( exception_type.__name__, value ) )
    logger.debug( '\n\n' + '\n'.join( traceback.format_tb(tb) ) )

def LogCommandTraceback( output ):
    #logger.error( "=== Exception: %s | %s" % ( exception, args ) )

    exception_type, value, tb = sys.exc_info()
    logger.error( "==== Exception: %s | %s ====" % ( exception_type.__name__, value ) )
    logger.debug( '\n\n' + '\n'.join( traceback.format_tb(tb) ) )

    output.write( "==== Exception: %s | %s ====" % ( exception_type.__name__, value ) )
    output.write( '\n\n' + '\n'.join( traceback.format_tb(tb) ) )

def LogOutputTraceback():
    #logger.error( "=== Exception: %s | %s" % ( exception, args ) )

    exception_type, value, tb = sys.exc_info()
    logger.error( "==== Exception: %s | %s ====" % ( exception_type.__name__, value ) )
    logger.debug( '\n\n' + '\n'.join( traceback.format_tb(tb) ) )

    output = "==== Exception: %s | %s ====" % ( exception_type.__name__, value )
    output = output + '\n\n' + '\n'.join( traceback.format_tb(tb) )
    return output

def LogJSONTraceback():
    exception_type, value, tb = sys.exc_info() #@UnusedVariable
    logger.error( "==== Exception: %s | %s ====" % ( exception_type.__name__, value ) )
    return { 'exception': '%s' % exception_type.__name__, 'message': '%s' % value }
