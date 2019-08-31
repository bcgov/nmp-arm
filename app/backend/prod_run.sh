#!/bin/bash

./manage.py migrate;
./manage.py loaddata initial_data; 
./manage.py runserver 0.0.0.0:8000;