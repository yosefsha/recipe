# Development stage
FROM python:3.11-alpine AS development

LABEL maintainer="sh.yosef@gmail.com"

WORKDIR /app

# Install dependencies first (before copying code for better caching)
COPY requirements.txt /tmp/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt && \
    apk del .tmp-build-deps

# Create user
RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Copy application code last (changes most frequently)
COPY --chown=django-user:django-user . /app

EXPOSE 8000

USER django-user

# Production stage
FROM python:3.11-alpine AS production

LABEL maintainer="sh.yosef@gmail.com"

WORKDIR /app

# Install dependencies first (before copying code for better caching)
COPY requirements.txt /tmp/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt && \
    apk del .tmp-build-deps

# Create user
RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Copy all necessary files (but will remove tests)
COPY --chown=django-user:django-user manage.py ./
COPY --chown=django-user:django-user core ./core
COPY --chown=django-user:django-user app ./app
RUN rm -rf ./app/tests

EXPOSE 8000

USER django-user

