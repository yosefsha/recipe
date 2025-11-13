FROM python:alpine3.22

LABEL maintainer="sh.yosef@gmail.com"

WORKDIR /app
COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

EXPOSE 8000

RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user

