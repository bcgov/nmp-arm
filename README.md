# Application Risk Management (NMP-ARM)

## Introduction

Applying manure at the wrong time and the wrong place poses risks to water quality for aquatic life and drinking water. Up until recently, farmers in coastal B.C. had no easy method to assess the environmental risks of nutrient (manure) application on a real-time site-specific, basis. Furthermore, farmers had no standard method to document the rationale for environmentally responsible nutrient applications.
 
The Ministry of Agriculture has the opportunity to adapt Whatcom Conservation District’s (WCD) “Application Risk Management” smart form app (https://www.whatcomcd.org/arm), with permission from WCD. The app provides a risk rating to users who must answer questions about factors (soil, crop, and weather conditions) that affect the environmental risk of nutrient application to a particular field on a given day. Once all the questions are answered with valid responses, the smart form allows the user to document the results as PDF that can be saved locally or shared by email from the app.

## History

### Backend
Although not documented, the legacy app's `/venv/requirements.txt` implies the following dependencies:  
```
Django==1.6
django-extensions
python-dateutil
django-timezone-field
pygments
importlib
```

In addition, the legagy app's `/venv/pyvenv/lib/python2.6` implies Python version 2.6.

### Apache Configuration
In terms of codebase, there appears to be a common codebase that serves out the Whatcom and the BC version of the app.  The legacy app already had a 'BC-specific' side to the app :

`conf/apache.conf`   : https://arm.local  
`conf/bc_apache.conf`: https://bc.arm.local 

### Database Configuration

There appears to be a PostgreSQL database (version yet to be determined), with a connection string of:
```
'HOST': 'localhost',
'PORT': '5432',
'NAME': 'arm',
```

### Obfuscated credentials

The original codebase had hardcoded account credentials, which have been replaced temporarily with tokens.  The details are:

```diff
[garywong@ncm050128 bc-arm (master)]$ git diffstat
arm/settings_overrides/dev.py | 14 +++++++-------
arm/settings_overrides/greg.py | 14 +++++++-------
conf/apache.conf | 8 ++++----
conf/bc_apache.conf | 8 ++++----
4 files changed, 22 insertions(+), 22 deletions(-)
[garywong@ncm050128 bc-arm (master)]$ git diff
diff --git a/arm/settings_overrides/dev.py b/arm/settings_overrides/dev.py
index 93bcce5..b4086ef 100755
--- a/arm/settings_overrides/dev.py
+++ b/arm/settings_overrides/dev.py
@@ -13,7 +13,7 @@ TEMPLATE_DEBUG = DEBUG
ABSOLUTE_PATH = os.path.dirname( __file__ ).replace( 'inout_board/settings_overrides', '' )

ADMINS = (
- ('Admin', 'user@gmail.com'),
+ ('Admin', '<admin.email@domain>'),
)

ALLOWED_HOSTS = [ 'localhost', 'inoutboard.local', 'maps.whatcomcd.org/inout/', socket.gethostname() ]
@@ -28,14 +28,14 @@ DATABASES = {
'HOST': 'localhost',
'PORT': '5432',
'NAME': 'inout_board',
- 'USER': 'user',
- 'PASSWORD': 'password',
+ 'USER': '<user>',
+ 'PASSWORD': '<password>',
},
}

-DEFAULT_FROM_EMAIL = 'user@gmail.com'
+DEFAULT_FROM_EMAIL = '<admin.email@domain>'

-EMAIL_TO='user@gmail.com'
+EMAIL_TO='<admin.email@domain>'

FIXTURE_DIRS = ( os.path.join( os.path.dirname( __file__ ), 'fixtures', 'dev' ).replace('\\','/'), )

@@ -136,11 +136,11 @@ LOGGING = {
},
}

-SERVER_EMAIL="user@gmail.com"
+SERVER_EMAIL="<admin.email@domain>"

SITE_ID = 4

-SUPPORT_EMAIL='user@gmail.com'
+SUPPORT_EMAIL='<admin.email@domain>'

'''
sys.stdout.write(
diff --git a/arm/settings_overrides/greg.py b/arm/settings_overrides/greg.py
index 93e8386..2b555ac 100755
--- a/arm/settings_overrides/greg.py
+++ b/arm/settings_overrides/greg.py
@@ -13,7 +13,7 @@ TEMPLATE_DEBUG = DEBUG
ABSOLUTE_PATH = os.path.dirname( __file__ ).replace( 'arm/settings_overrides', '' )

ADMINS = (
- ('Admin', 'user@gmail.com'),
+ ('Admin', '<admin.email@domain>'),
)

ALLOWED_HOSTS = [ 'localhost', 'arm.local', 'maps.whatcomcd.org/arm/', socket.gethostname() ]
@@ -28,14 +28,14 @@ DATABASES = {
'HOST': 'localhost',
'PORT': '5432',
'NAME': 'arm',
- 'USER': 'user',
- 'PASSWORD': 'password',
+ 'USER': '<user>',
+ 'PASSWORD': '<password>',
},
}

-DEFAULT_FROM_EMAIL = 'user@gmail.com'
+DEFAULT_FROM_EMAIL = '<admin.email@domain>'

-EMAIL_TO='user@gmail.com'
+EMAIL_TO='<admin.email@domain>'

FIXTURE_DIRS = ( os.path.join( os.path.dirname( __file__ ), 'fixtures', 'dev' ).replace('\\','/'), )

@@ -136,11 +136,11 @@ LOGGING = {
},
}

-SERVER_EMAIL="user@gmail.com"
+SERVER_EMAIL="<admin.email@domain>"

SITE_ID = 4

-SUPPORT_EMAIL='user@gmail.com'
+SUPPORT_EMAIL='<admin.email@domain>'

'''
sys.stdout.write(
diff --git a/conf/apache.conf b/conf/apache.conf
index bf88062..ad8ed95 100755
--- a/conf/apache.conf
+++ b/conf/apache.conf
@@ -5,7 +5,7 @@
SSLCACertificateFile /etc/apache2/ssl/gd_bundle-g2-g1.crt

ServerName arm.local
- ServerAdmin user@gmail.com
+ ServerAdmin <admin.email@domain>
DocumentRoot "/usr/local/src/arm_working_directory"


@@ -28,10 +28,10 @@

SetEnv ENVIRONMENT greg
SetEnv ARMDBNAME arm
- SetEnv ARMDBUSER user
- SetEnv ARMDBPASS password
+ SetEnv ARMDBUSER <user>
+ SetEnv ARMDBPASS <password>

diff --git a/conf/bc_apache.conf b/conf/bc_apache.conf
index 9255484..a2de963 100755
--- a/conf/bc_apache.conf
+++ b/conf/bc_apache.conf
@@ -5,7 +5,7 @@
SSLCACertificateFile /etc/apache2/ssl/gd_bundle-g2-g1.crt

ServerName bc.arm.local
- ServerAdmin user@gmail.com
+ ServerAdmin <admin.email@domain>
DocumentRoot "/usr/local/src/bc_arm_working_directory"

@@ -28,10 +28,10 @@

SetEnv ENVIRONMENT greg
SetEnv ARMDBNAME arm
- SetEnv ARMDBUSER user
- SetEnv ARMDBPASS password
+ SetEnv ARMDBUSER <user>
+ SetEnv ARMDBPASS <password>

[garywong@ncm050128 bc-arm (master)]$ 
```