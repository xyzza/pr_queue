#!/bin/bash

NAME="prqueue"
DJANGODIR=/var/www/pull_requests/prqueue
SOCKFILE=/var/www/pull_requests/gunicorn/sock/gunicorn.sock
USER=www-data
GROUP=www-data
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=prqueue.settings
DJANGO_WSGI_MODULE=prqueue.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
workon pull_requests
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-