import logging
logger = logging.getLogger( __file__ )

class DBRouter(object):
    """A router to control all database operations on models in
    the contrib.auth application"""

    def db_for_read( self, model, **hints):
        if hasattr( model._meta, 'db_connection' ):
            return model._meta.db_connection
        return None

    def db_for_write(self, model, **hints):
        if hasattr( model._meta, 'db_connection' ):
            return model._meta.db_connection
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        if obj1._meta.db_connection == obj2._meta.db_connection:
            return True
        return False

    def allow_syncdb(self, db, model):
        if hasattr( model._meta, 'db_connection' ):
            return db == model._meta.db_connection
        return db == 'default'
