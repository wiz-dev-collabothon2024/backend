#!/bin/bash

# Apply migrations
python manage.py makemigrations
python manage.py migrate

pytest -v

# Start Django server
python manage.py runserver 0.0.0.0:8000