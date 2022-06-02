FROM python:3.9.6 AS base

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get -y install bluetooth libbluetooth-dev

RUN pip install --upgrade pip

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app

ENV PYTHONPATH=/app:$PYTHONPATH

ADD . /app

CMD [ "/app/scripts/django-startup.sh" ]

################ dev
FROM base as dev

ADD requirements.dev.txt /requirements.dev.txt
RUN pip install -r /requirements.dev.txt
