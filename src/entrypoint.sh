#!/bin/sh

export DJANGO_SETTINGS_MODULE=conf.settings

if [ "$DJANGO_STATIC" = 1 ]; then
  python manage.py collectstatic --noinput
fi

if [ "$DJANGO_MIGRATE" = 1 ]; then
    if [ "$POSTGRES_HOST" != "" ]; then
        echo "Waiting for postgres..."
        sleep 7.77
        echo "PostgreSQL started"
    fi
    python manage.py migrate
fi

if [ "$DJANGO_WEB" = 1 ]; then
    python manage.py runserver 0.0.0.0:8000
fi
