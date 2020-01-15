
import sys
import os
sys.path.append("...")

def turnOff():
    print('Turning off with turn_off.py')
    #change CONTAINER-NAME at the end of the next line. You can also change /stop-service to /restart-service
    os.system('curl --header "Content-Type:application/json" "$BALENA_SUPERVISOR_ADDRESS/v2/applications/$BALENA_APP_ID/stop-service?apikey=$BALENA_SUPERVISOR_API_KEY" -d \'{"serviceName": "CONTAINER-NAME"}\'')

turnOff()