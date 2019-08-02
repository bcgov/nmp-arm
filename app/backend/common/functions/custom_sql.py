import logging
logger = logging.getLogger( __file__ )

def CustomSQLQuery( sql, args ):
    from django.db import connection
    cursor = connection.cursor()

    # Data retrieval operation - no commit required
    cursor.execute( sql, args )
    rows = cursor.fetchall()
    cursor.execute( "COMMIT" )

    return rows

def CustomStoredProcedureQuery( sql, args ):

    from django.db import connection
    from datetime import datetime
    from time import mktime

    referer = 'ref%s' % int( mktime( datetime.now().timetuple() ) )
    new_args = ( referer, ) + args

    cursor = connection.cursor()
    cursor.execute( "BEGIN" )
    sql_statement = sql % new_args
    logger.debug( "sql = %s" % sql_statement )
    cursor.execute( sql_statement )
    cursor.execute( "FETCH ALL IN %s" % referer )
    results = cursor.fetchall()
    cursor.execute( "COMMIT" )

    return results
