#!/usr/bin/env bash

copy_env_file_if_not_exists () {
  if [ ! -f .env ]; then
    echo "'.env' file not found"
    echo "Copying '.env.example' to '.env' ..."
    cp .env.example .env
  else
    echo "Using existing '.env' file"
  fi
}

wait_for_pg () {
  echo "START: wait_for_pg"
  echo "TODO"  #  TODO
#  echo "host=${POSTGRES_HOST}, port=${POSTGRES_PORT}, name=${POSTGRES_DB}"
#  echo "Waiting for PostgreSQL to start..."
#  while ! nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
#    sleep 0.1
#  done
  echo "END: wait_for_pg"
}

setup_db () {
  echo "START: setup_db"
  python manage.py create_initial_admin
  python manage.py migrate
  echo "END: setup_db"
}

collect_static () {
  echo "START: collect_static"
  python manage.py collectstatic --no-input
  echo "END: collect_static"
}
