#!/bin/bash

NAME=prqueue
VENVDIR=/var/www/.virtualenvs/pull_requests/bin/
PROJECTDIR=/var/www/pull_requests/prqueue/
SOCKFILE=/var/www/pull_requests/run/gunicorn.sock
USER=edu-admin
GROUP=edu-admin
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=prqueue.settings
DJANGO_WSGI_MODULE=prqueue.wsgi

echo "Starting $NAME as `whoami`"

$VENVDIR/activate

#export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
#export PYTHONPATH=$PROJECTDIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

cd $PROJECTDIR
exec $VENVDIR/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --env DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=INFO \
  --log-file=-
