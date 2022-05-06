FROM python:slim

LABEL maintainer="smaeil0018@gmail.com"
LABEL version="1.0.0"
LABEL description="Cache Service"

ENV PYTHONPATH=. TZ="Asia/Tehran" 

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install Wikipedia-API

COPY . .
