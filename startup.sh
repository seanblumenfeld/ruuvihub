#!/usr/bin/env bash

python manage.py migrate

python manage.py run_huey &

python manage.py runserver ${DJANGO_HOST}:${DJANGO_PORT}
