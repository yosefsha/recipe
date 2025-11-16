# Development stage
FROM python:3.11-alpine AS development

LABEL maintainer="sh.yosef@gmail.com"

WORKDIR /app

# Create user first
RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

COPY requirements.txt /tmp/requirements.txt
COPY --chown=django-user:django-user . /app

EXPOSE 8000

RUN pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt && \
    apk del .tmp-build-deps

USER django-user

# Production stage
FROM python:3.11-alpine AS production

LABEL maintainer="sh.yosef@gmail.com"

WORKDIR /app
COPY requirements.txt /tmp/requirements.txt

EXPOSE 8000

RUN pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Copy all necessary files (but will remove tests)
COPY --chown=django-user:django-user manage.py ./
COPY --chown=django-user:django-user core ./core
COPY --chown=django-user:django-user app ./app
RUN rm -rf ./app/tests

USER django-user

