#!/usr/bin/env bash

wait_for_pg () {
  echo "START: wait_for_pg"
  echo "TODO"  #  TODO
  sleep 3
#  echo "host=${POSTGRES_HOST}, port=${POSTGRES_PORT}, name=${POSTGRES_DB}"
#  echo "Waiting for PostgreSQL to start..."
#  while ! nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
#    sleep 0.1
#  done
  echo "END: wait_for_pg"
}

setup_db () {
  echo "START: setup_db"
  wait_for_pg
  python manage.py migrate
  python manage.py create_initial_admin
  echo "END: setup_db"
}

collect_static () {
  echo "START: collect_static"
  python manage.py collectstatic --no-input
  echo "END: collect_static"
}


###### RUN ######

echo "START: startup"

setup_db

python manage.py run_huey &

case ${ENV} in
  "test" | "dev")
    wait_for_pg
    python manage.py runserver ${HOST}:${PORT}
  ;;
  *)
    collect_static
    uwsgi --http-socket :${PORT} --module web.wsgi
  ;;
esac

echo "END: startup"
