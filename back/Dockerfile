FROM python:3.10-alpine

WORKDIR /usr/src/app

RUN apk add -U --no-cache mariadb-dev gcc g++ libc-dev
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

