#!/bin/bash
# Start Gunicorn processes
exec gunicorn geoxp.wsgi:application \
	--bind 0.0.0.0:8000 \
