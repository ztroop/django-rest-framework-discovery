FROM python:3.6-alpine

RUN apk update && \
    apk add --update \
    build-base sqlite openssl-dev && \
    rm -rf /var/cache/apk/*

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
ENV PYTHONPATH $PYTHONPATH:/app
COPY . /app
CMD gunicorn food_database_example.wsgi:application \
    --name food_database_example --bind 0.0.0.0:8080 --workers 3 --timeout=300

EXPOSE 8000
