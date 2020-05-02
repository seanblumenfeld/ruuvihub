FROM python:3.7.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get -y install bluetooth libbluetooth-dev

# Copy requirements file in separately to rest of project.
# This allows docker to cache requirements, and so only changes to
# requirements.txt will trigger a new pip install
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# TODO: move to test docker image for testing
ADD requirements.test.txt /requirements.test.txt
RUN pip install -r /requirements.test.txt

# TODO: remove once available in pypi
RUN pip install --upgrade git+git://github.com/ttu/ruuvitag-sensor.git@3dac6fc3843b258a8282f2909a9c74f4654d76b7

ADD . /app
WORKDIR /app

ENV PYTHONPATH=/app:$PYTHONPATH
