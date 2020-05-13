#!/usr/bin/env bash

echo "START: startup"

source scripts/utils.sh

setup_db
collect_static

case ${ENV} in
  "test" | "dev")
    wait_for_pg
    python manage.py runserver ${HOST}:${PORT}
  ;;
  *)
    uwsgi --http :${PORT} --module web.wsgi
  ;;
esac

echo "END: startup"
