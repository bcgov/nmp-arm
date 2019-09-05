#!/bin/bash


RUN rm -f /code/db.sqlite3

echo "Apply database migrations"
python manage.py migrate;

echo "Load data"
python manage.py loaddata initial_data; 

echo "Run server"
python manage.py runserver 0.0.0.0:80;