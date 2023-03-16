FROM python:3.9-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SENTRY_DSN $SENTRY_DSN

RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc libc-dev make && \
    pip install -r requirements.txt && \
    apk del .build-deps && \
    python manage.py collectstatic --noinput

COPY . /code/

# Expose the required ports
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
