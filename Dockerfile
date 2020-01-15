FROM balenalib/raspberrypi3-alpine

#WORKDIR /usr/src

# Install python 3 and balena SDK dependencies.
RUN install_packages build-base python3 py3-setuptools python3-dev libffi-dev openssl-dev

# Install balena python SDK in python 3.
RUN pip3 install balena-sdk

RUN install_packages wget unzip curl

# Copy files over and make bash and python files executible
COPY scripts /usr/src/
RUN chmod +x /usr/src/*.sh
RUN chmod +x /usr/src/*.py

CMD /usr/src/start.sh