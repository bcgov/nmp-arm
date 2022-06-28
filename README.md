# Application Risk Management (NMP-ARM)

## Introduction

Applying manure at the wrong time and the wrong place poses risks to water quality for aquatic life and drinking water. Up until recently, farmers in coastal B.C. had no easy method to assess the environmental risks of nutrient (manure) application on a real-time site-specific, basis. Furthermore, farmers had no standard method to document the rationale for environmentally responsible nutrient applications.
 
The Ministry of Agriculture has the opportunity to adapt Whatcom Conservation District’s (WCD) “Application Risk Management” smart form app (https://www.whatcomcd.org/arm), with permission from WCD. The app provides a risk rating to users who must answer questions about factors (soil, crop, and weather conditions) that affect the environmental risk of nutrient application to a particular field on a given day. Once all the questions are answered with valid responses, the smart form allows the user to document the results as PDF that can be saved locally or shared by email from the app.

## Getting started

### Prerequisities

* Python 3
* Docker

### Running ARM locally

1. Make a copy of `.env.sample`, and rename it to `.env`:

    ```sh
    cd nmp-arm
    cp .env.sample .env
    ```

2. The provided SMTP server (`apps.smtp.gov.bc.ca`) is [only accessible from inside the government datacentre](https://stackoverflow.developer.gov.bc.ca/questions/233/244#244), so you'll have to provide your own SMTP server for local testing. To do so, edit the following entries in `.env` as appropriate:
    ```
    DEFAULT_FROM_EMAIL
    EMAIL_HOST
    EMAIL_PORT
    EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD
    ```
    **Note:** By default, Gmail does not allow SMTP access unless a [less-secure "app password"](https://support.google.com/mail/answer/185833?hl=en) is configured. Services such as [Mailgun](https://www.mailgun.com/) can be used instead.
   
3. Run via docker-compose:

    ```sh
    cd nmp-arm 
    docker-compose up
    ```

The application can be accessed at http://localhost:8000. To quit, simply hit Ctrl-C in the terminal.

## History

This section was written by the previous devs, presumably as part of an investigation into setting up the app and/or updating its components.

It is left here for historical context. Please refer to the "Getting Started" section for up-to-date setup instructions.

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

In addition, the legacy app's `/venv/pyvenv/lib/python2.6` implies Python version 2.6.

NOTE: `Django==1.6` results in:
```
ERROR: django-timezone-field 3.0 has requirement django>=1.8, but you'll have django 1.6 which is incompatible.
```

So `Django==1.8` is a more appropriate starting point.

### Post Upgrade to Python 3.7 and Django 2.2.4

### Requirements
```
Django==2.2.4
django-extensions
python-dateutil
django-timezone-field
pygments
psycopg2
python-decouple
```

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
