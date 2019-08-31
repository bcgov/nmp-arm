# -*- coding: utf-8 -*-

#
#  django imports
#
from django.conf import settings
#from django.db.models.signals import post_syncdb
from django.db import connection, transaction
from django.dispatch import receiver

#
#  sys imports
#
from glob import glob
import logging
import os
logger = logging.getLogger( __file__ )

'''
@receiver( post_syncdb )
def modify_database( sender, **kwargs ):
    
    cursor = connection.cursor()

    raw_sql_dir = os.path.join( settings.ABSOLUTE_PATH, settings.SETTINGS_MODULE.replace( '.settings', '' ), 'settings_overrides', 'raw_sql' )

    if os.path.isdir( raw_sql_dir ):
        # Add Stored Procedures
        for filename in sorted( glob( os.path.join( raw_sql_dir, '*.sql' ) ) ):
            #logger.debug( filename )
            f = open( os.path.join( raw_sql_dir, filename ) )
            query = f.read()
            #print query
            cursor.execute( query )
            print "Added SQL from file: [%s]" % filename
'''

