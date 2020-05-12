#!/usr/bin/env bash

python manage.py migrate

case ${ENV} in
    "test" | "dev")
        python manage.py runserver ${DJANGO_HOST}:${DJANGO_PORT}
    ;;
    *)
        uwsgi --http :8000 --module web.wsgi
    ;;
esac
