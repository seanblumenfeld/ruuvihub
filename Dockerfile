FROM python:3.7.6 AS base

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get -y install bluetooth libbluetooth-dev

RUN pip install --upgrade pip

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# TODO: remove once available in pypi
RUN pip install --upgrade git+git://github.com/ttu/ruuvitag-sensor.git@3dac6fc3843b258a8282f2909a9c74f4654d76b7

WORKDIR /app

ENV PYTHONPATH=/app:$PYTHONPATH

ADD . /app

CMD [ "/app/scripts/django-startup.sh" ]

################ dev
FROM base as dev

ADD requirements.dev.txt /requirements.dev.txt
RUN pip install -r /requirements.dev.txt
