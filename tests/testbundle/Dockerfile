FROM alpine:3.6

MAINTAINER Diogenes Santos de Jesus <diogenes.jesus@telekom.com>

# Install python3
RUN apk update && \
    apk add --no-cache python3 git && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

# Install newer certs and pycog3
RUN apk add ca-certificates wget && \
  ln -s /usr/bin/python3 /usr/bin/python

RUN adduser -h /home/bundle -D bundle

USER root

RUN mkdir -p /home/module/pycog3/

COPY pycog3/                 /home/module/pycog3/
COPY pycog3/cog/             /home/module/pycog3/cog/
COPY pycog3/bin/             /home/module/pycog3/bin/

WORKDIR /home/module/pycog3

RUN pip3 install -r requirements.txt
RUN pip3 install .

RUN mkdir -p /home/bundle/testbundle/testbundle/

COPY setup.py requirements.txt  /home/bundle/testbundle/
COPY testbundle/                /home/bundle/testbundle/testbundle/

WORKDIR /home/bundle/testbundle

RUN pip3 install .

RUN apk del git
RUN rm -rfv /home/bundle/testbundle  \
            /home/module/ \
            /var/cache/apk/*  \
            /root/.cache

WORKDIR /home/bundle/
USER bundle