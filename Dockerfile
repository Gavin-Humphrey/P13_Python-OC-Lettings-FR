FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apk add --no-cache --virtual .build-deps gcc libc-dev make && \
    pip install -r requirements.txt && \
    apk del .build-deps
COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
