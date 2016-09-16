#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn geoxp.wsgi:application \
    --bind 0.0.0.0:$PORT
