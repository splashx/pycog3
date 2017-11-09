FROM python:3.6.3

USER root

RUN mkdir -p /home/pycog3/

COPY setup.py requirements.txt  /home/pycog3/
COPY ./cog/                     /home/pycog3/cog/
COPY ./bin/                     /home/pycog3/bin/
COPY ./tests/                     /home/pycog3/tests/

WORKDIR /home/pycog3

RUN pip3 install -r requirements.txt
RUN pip3 install .

RUN mkdir -p /home/bundle/testbundle/testbundle/

COPY tests/testbundle/setup.py         /home/bundle/testbundle/
COPY tests/testbundle/testbundle/      /home/bundle/testbundle/testbundle/

WORKDIR /home/bundle/testbundle

RUN pip3 install .

RUN rm -rf /home/bundle/testbundle

WORKDIR /home/pycog3

