import os
import socket
import sys
import logging
logger = logging.getLogger( __file__ )


# Debugging flags:
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Settings below (Alphabetically)
ABSOLUTE_PATH = os.path.dirname( __file__ ).replace( 'arm/settings_overrides', '' )

ADMIN_EMAIL=os.environ.get( 'ADMIN_EMAIL' )
# ADMINS = (
#     ('Admin', ADMIN_EMAIL),
# )

ALLOWED_HOSTS = [ 'localhost', 'inoutboard.local', 'maps.whatcomcd.org/inout/', socket.gethostname() ]

# MANAGERS = ADMINS

DATABASE_NAME = os.environ.get( 'DATABASE_NAME' )
DATABASE_USER = os.environ.get( 'DATABASE_USER' )
DATABASE_PASSWORD = os.environ.get( 'DATABASE_PASSWORD' )

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         #'ENGINE': 'django.db.backends.sqlite3',
#         #'HOST': 'postgis91.pugetworks.com',
#         'HOST': 'localhost',
#         'PORT': '5432',
#         'NAME': DATABASE_NAME,
#         'USER': DATABASE_USER,
#         'PASSWORD': DATABASE_PASSWORD,
#     },
# }

DEFAULT_FROM_EMAIL = os.environ.get( 'DEFAULT_FROM_EMAIL' )

EMAIL_TO = os.environ.get( 'EMAIL_TO' )

FIXTURE_DIRS = ( os.path.join( os.path.dirname( __file__ ), 'fixtures', 'dev' ).replace('\\','/'), )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'audit_true': {
            '()': 'common.classes.AuditLogFilters.AuditLogFilterTrue',
        },
        'audit_false': {
            '()': 'common.classes.AuditLogFilters.AuditLogFilterFalse',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'minimal': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'audit_format': {
            'format': '%(asctime)s %(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': [ 'console', 'file_logging' ],
            'level': 'DEBUG',
            'propogate': True,
        },
        'django' : {
            'handlers': ['file_logging'],
            'level' : 'DEBUG',
            'propagate' : True,
        },
        'django.db' : {
            'handlers' : ['db_logging'],
            'level' : 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'minimal',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': [ 'require_debug_false' ],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file_logging': {
            'level' : 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'backupCount' : 5,
            'maxBytes': 1024 * 1024 * 5, # 5 mb
            'filename': os.path.join( ABSOLUTE_PATH, 'logs', 'django.log').replace('\\','/'),
            'formatter': 'verbose',
        },
        'db_logging': {
            'level' : 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'backupCount' : 5,
            'maxBytes': 1024 * 1024 * 5, # 5 mb
            'filename': os.path.join( ABSOLUTE_PATH, 'logs', 'django-db.log').replace('\\','/'),
        },
        'audit_logging': {
            'level' : 'INFO',
            'filters': ['audit_true'],
            'class' : 'logging.handlers.RotatingFileHandler',
            'formatter': 'audit_format',
            'backupCount' : 5,
            'maxBytes': 1024 * 1024 * 5, # 5 mb
            'filename': os.path.join( ABSOLUTE_PATH, 'logs', 'audit.log').replace('\\','/'),
        },
    },
}

SERVER_EMAIL = os.environ.get( 'SERVER_EMAIL' )

SITE_ID = 4

SUPPORT_EMAIL = os.environ.get( 'SUPPORT_EMAIL' )

'''
sys.stdout.write(
    '[ APACHE INFO ] {0} {1} {2} {3}'.format(
        os.environ.get( 'ENVIRONMENT' ),
        os.environ.get( 'INOUTDBNAME' ),
        os.environ.get( 'INOUTDBUSER' ),
        os.environ.get( 'INOUTDBPASS' ),
    )
)
'''


