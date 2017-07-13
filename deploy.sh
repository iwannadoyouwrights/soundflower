#!/bin/sh
# Run:
# sh deploy.sh && .env/bin/python manage.py runserver

set -e

rm -rf .env && virtualenv -p $(which python3) .env && .env/bin/pip install -r requirements.txt
python=.env/bin/python

rm -rf db.sqlite3
# $python manage.py makemigrations
$python manage.py migrate
$python manage.py createsuperuser
