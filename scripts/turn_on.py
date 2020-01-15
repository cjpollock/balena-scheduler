
import sys
import os
sys.path.append("...")

def turnOn():
    print('Turning on in turn_on.py')
    # Uncomment next line to just restart your container. You can copy/paste this for multiple containers.
    #os.system('curl --header "Content-Type:application/json" "$BALENA_SUPERVISOR_ADDRESS/v2/applications/$BALENA_APP_ID/start-service?apikey=$BALENA_SUPERVISOR_API_KEY" -d \'{"serviceName": "CONTAINER-NAME"}\'')
    
    os.system('curl -X POST --header "Content-Type:application/json" "$BALENA_SUPERVISOR_ADDRESS/v1/reboot?apikey=$BALENA_SUPERVISOR_API_KEY"')
    # I prefer to reboot the whole device instead of just starting containers. Feel free to comment out previous line if this doesn't work for you. 

turnOn()