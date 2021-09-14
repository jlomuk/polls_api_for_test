#!/usr/bin/env bash
while ! python manage.py migrate --no-input 2>&1; do
  sleep 3
done
while ! python manage.py loaddata fixtures.json  2>&1; do
   sleep 3
done
exec "$@"
