#!/usr/bin/env bash

sed -e 's|<HTTP_PORT>|'${PORT}'|' -i /etc/grafana/grafana.ini
sed -e 's|<DATABASE_URL>|'${DATABASE_URL}'|' -i /etc/grafana/grafana.ini
sed -e 's|<ADMIN_USER>|'${ADMIN_USER}'|' -i /etc/grafana/grafana.ini
sed -e 's|<ADMIN_PASSWORD>|'${ADMIN_PASSWORD}'|' -i /etc/grafana/grafana.ini

/run.sh