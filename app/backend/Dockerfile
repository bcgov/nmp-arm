# set the base image 
FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -U pip
RUN pip install -Ur requirements.txt

EXPOSE 8000