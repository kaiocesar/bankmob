FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /core
WORKDIR /core

ADD requeriments.txt /core/
RUN pip install --upgrade pip && pip install -r requeriments.txt
ADD . /core/