#!/bin/bash

if [ "$ENABLE_TIMER" == "1" ]
then
  echo "Starting scheduler."
  (crontab -l; echo "${TURN_ON:-0 8 * * *} python3 /usr/src/turn_on.py") | crontab -
  (crontab -l; echo "${TURN_OFF:-0 23 * * *} python3 /usr/src/turn_off.py") | crontab -
fi

crond -f