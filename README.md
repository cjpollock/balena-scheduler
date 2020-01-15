# balena-scheduler
This code will allow you to start and stop a service at a certain time in Balena. Tested with RPi 3 &amp; 4. 

Make sure the docker-compose file adds the label: io.balena.features.supervisor-api: '1'

SAMPLE: 

  scheduler:
    build: ./scheduler
    restart: always
    privileged: true
    labels:
      io.balena.features.supervisor-api: '1'
