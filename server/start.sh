#! /usr/bin/env sh
set -e

if [ -f /app/app/main.py ]; then
    DEFAULT_MODULE_NAME=app/main.py
elif [ -f /app/main.py ]; then
    DEFAULT_MODULE_NAME=main.py
fi
export MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}

# If there's a prestart.sh script in the /app directory or other path specified, run it before starting
PRE_START_PATH=${PRE_START_PATH:-/app/prestart.sh}
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else 
    echo "There is no script $PRE_START_PATH"
fi

# Start Gunicorn
exec fastapi run "$MODULE_NAME"
