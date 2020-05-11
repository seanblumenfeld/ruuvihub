#!/usr/bin/env bash

python manage.py migrate

python manage.py runserver ${DJANGO_HOST}:${DJANGO_PORT}
