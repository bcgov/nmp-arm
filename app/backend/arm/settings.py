from threading import Lock
import os, sys
import socket
from decouple import config
import logging

logger = logging.getLogger(__file__)

# Debugging flags:
DEBUG = config('DEBUG', default='True', cast=bool)

# Absolute filesystem path to the project.
ABSOLUTE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_EMAIL = config('ADMIN_EMAIL', default='')
ADMINS = (
    ('Admin', ADMIN_EMAIL),
)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', socket.gethostname(), '.azurewebsites.net']

# AUTH_USER_MODEL = 'admins.Admin'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
# MANAGERS = ADMINS

DATABASE_HOST = config('DATABASE_HOST')
DATABASE_NAME = config('DATABASE_NAME')
DATABASE_USER = config('DATABASE_USER')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ABSOLUTE_PATH, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'HOST': 'localhost',
        # 'PORT': '5432',
        # 'NAME': DATABASE_NAME,
        # 'USER': DATABASE_USER,
        # 'PASSWORD': DATABASE_PASSWORD,
    },
}


DATE_FORMAT = 'N j, Y'
DATE_TIME_FORMAT = 'N j, Y, P'

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

TIME_FORMAT = 'H:i P'

# Mail Server info
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = 'tmp/email-messages/'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 25
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = 1
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

EMAIL_TO = config('EMAIL_TO')

ENVIRONMENT = config('ENVIRONMENT')

FIXTURE_DIRS = (os.path.join(os.path.dirname(__file__), 'fixtures', 'dev'),)

# FORCE_SCRIPT_NAME='arm'
USE_X_FORWARDED_HOST = True

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

    'arm',  # for management commands
    # 'arm.calc' ,
)

LANGUAGE_CODE = 'en-us'

# Lock implementation
LOCK = Lock()

LOGIN_URL = '/admin/'
LOGIN_REDIRECT_URL = '/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGER_LEVEL = config('LOGGER_LEVEL', default='DEBUG')
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
            'handlers': ['console', 'file_logging'],
            'level': LOGGER_LEVEL,
            'propogate': True,
        },
        'django': {
            'handlers': ['file_logging'],
            'level': LOGGER_LEVEL,
            'propagate': True,
        },
        'django.db': {
            'handlers': ['db_logging'],
            'level': LOGGER_LEVEL,
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
            'level': LOGGER_LEVEL,
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': LOGGER_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'minimal',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file_logging': {
            'level': LOGGER_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 5,
            'maxBytes': 1024 * 1024 * 5,  # 5 mb
            'filename': os.path.join(ABSOLUTE_PATH, 'logs', 'django.log'),
            'formatter': 'verbose',
        },
        'db_logging': {
            'level': LOGGER_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 5,
            'maxBytes': 1024 * 1024 * 5,  # 5 mb
            'filename': os.path.join(ABSOLUTE_PATH, 'logs', 'django-db.log'),
        },
        'audit_logging': {
            'level': 'INFO',
            'filters': ['audit_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'audit_format',
            'backupCount': 5,
            'maxBytes': 1024 * 1024 * 5,  # 5 mb
            'filename': os.path.join(ABSOLUTE_PATH, 'logs', 'audit.log'),
        },
    },
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(ABSOLUTE_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'common.classes.SessionExpiryMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# MOBILE keys
APNS_CERT = 'full_path'
APNS_SANDBOX = True

GCM_API_KEY = '<>'

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
SECRET_KEY = '<>'

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
SESSION_EXPIRY = (259200 * 20)

SERVER_EMAIL = config('SERVER_EMAIL')

SITE_ID = 4

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ABSOLUTE_PATH, 'static/'),
)

SUPPORT_EMAIL = config('SUPPORT_EMAIL')

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Los_Angeles'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(ABSOLUTE_PATH, 'templates', 'html'),
            os.path.join(ABSOLUTE_PATH, 'templates', 'emails'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

USE_ETAGS = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Where imports are uploaded to
UPLOAD_DIR = os.path.join(ABSOLUTE_PATH, 'media', 'uploads')

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'arm.wsgi.application'
