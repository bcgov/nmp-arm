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

NOTE: `Django==1.6` results in:
```
ERROR: django-timezone-field 3.0 has requirement django>=1.8, but you'll have django 1.6 which is incompatible.
```

So `Django==1.8` is a more appropriate starting point.

### Post Upgrade to Python 3.7 and Django 2.2.4

### Requirements
Django==2.2.4
django-extensions
python-dateutil
django-timezone-field
pygments
psycopg2
python-decouple

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

### Required Environment Variables

      ENVIRONMENT: dev
      DEBUG: 'False'
      LOGGER_LEVEL: WARNING
      ADMIN_EMAIL: admin.email@domain
      DATABASE_NAME:  DATABASE_NAME
      DATABASE_USER: DATABASE_USER
      DATABASE_PASSWORD: DATABASE_PASSWORD
      DEFAULT_FROM_EMAIL: admin.email@domain
      EMAIL_TO: admin.email@domain
      SERVER_EMAIL: admin.email@domain
      SUPPORT_EMAIL: admin.email@domain