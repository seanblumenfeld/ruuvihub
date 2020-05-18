#!/usr/bin/env bash

sed -i -e 's|<HTTP_PORT>|'$PORT'|' /etc/grafana/grafana.ini
sed -i -e 's|<DATABASE_URL>|'$DATABASE_URL'|' /etc/grafana/grafana.ini
sed -i -e 's|<ADMIN_PASSWORD>|'$ADMIN_PASSWORD'|' /etc/grafana/grafana.ini

/run.sh