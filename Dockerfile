FROM python:3.7.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get -y install bluetooth libbluetooth-dev

# Copy requirements file in separately to rest of project.
# This allows docker to cache requirements, and so only changes to
# requirements.txt will trigger a new pip install
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# TODO: move to dev docker image for local development
ADD requirements.dev.txt /requirements.dev.txt
RUN pip install -r /requirements.dev.txt

ADD . /app
WORKDIR /app

ENV PYTHONPATH=/app:$PYTHONPATH
