from django.utils.importlib import import_module
from threading import Lock
import warnings
import os, sys
import logging
logger = logging.getLogger( __file__ )

# Absolute filesystem path to the project.
ABSOLUTE_PATH = os.path.dirname( __file__ ).replace( '/arm/', '/' )

AUTH_USER_MODEL = 'admins.Admin'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

DATE_FORMAT = 'N j, Y'
DATE_TIME_FORMAT = 'N j, Y, P'

TIME_FORMAT = 'H:i P'

# Mail Server info
EMAIL_HOST='localhost'
EMAIL_PORT=25

ENVIRONMENT=os.environ.get( 'ENVIRONMENT' )

FORCE_SCRIPT_NAME='/arm'
USE_X_FORWARDED_HOST = True

LANGUAGE_CODE = 'en-us'

# Lock implementation
LOCK=Lock()

LOGIN_URL='/admin/'
LOGIN_REDIRECT_URL='/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join( ABSOLUTE_PATH, '..', 'media/').replace('\\','/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'common.classes.SessionExpiryMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# MOBILE keys
APNS_CERT='full_path'
APNS_SANDBOX=True

GCM_API_KEY='AIzaSyDeWyzBpPHoVg33NkFk8v65z9T-thv4GX8'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

ROOT_URLCONF = 'arm.urls'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm3rl^x8%ly=hui2o2q6@h8g&amp;d4qsx1qwex%_lop)4s!=qz0pzr'

SESSION_COOKIE_HTTPONLY = True

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# Tell browser to delete cookie on browser close
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True

#
# 10800 seconds is 3 hour expirey
# 600 seconds is 10 min expirey
# 259200 three day expirey
#
SESSION_EXPIRY = ( 259200 * 20 )

SESSION_SAVE_EVERY_REQUEST = True

SERVERVERSION = '0.0.1'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join( ABSOLUTE_PATH, 'static' ).replace('\\','/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

USE_ETAGS = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Los_Angeles'

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages")


TEMPLATE_DIRS = (
    os.path.join( ABSOLUTE_PATH, '..', 'templates', 'html' ).replace('\\','/'),
    os.path.join( ABSOLUTE_PATH, '..', 'templates', 'emails' ).replace('\\','/'),
)
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# Where imports are uploaded to
UPLOAD_DIR = os.path.join( ABSOLUTE_PATH, 'media', 'uploads' ).replace('\\','/')

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'arm.settings_overrides.dev_wsgi'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    # for extended manager options
    'django_extensions',

    'common',

    # api or alternate view functionality
    'conduit',

    # For admin functionality
    'admins',

    'arm', # for management commands
    #'arm.calc' ,
)

def override_settings( dottedpath ):
    try:
        _m = import_module( dottedpath )
    except ImportError:
        warnings.warn( "Failed to import environment settings: %s" % dottedpath )
        pass
    else:
        _thismodule = sys.modules[__name__]
        for _k in dir(_m):
            if _k.isupper() and not _k.startswith('__'):
                setattr( _thismodule, _k, getattr( _m, _k ) )

override_settings( 'arm.settings_overrides.%s' % ENVIRONMENT )
