# set the base image 
FROM python:latest

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -U pip
RUN pip install -Ur requirements.txt


# Collect our static media.
# RUN python /code/manage.py collectstatic --noinput

### Containers should not run as root as a good practice
USER root
RUN chmod +x ./prod_run.sh

USER 10001

ENTRYPOINT [ "sh", "./prod_run.sh" ]