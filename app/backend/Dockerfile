# set the base image 
FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -U pip
RUN pip install -Ur requirements.txt


# Collect our static media.
# RUN python /code/manage.py collectstatic --noinput

### Containers should not run as root as a good practice
# USER root
#RUN chmod +x ./prod_run.sh

#ENTRYPOINT [ "./prod_run.sh" ]

# RUN python /code/manage.py migrate;
# RUN python /code/manage.py loaddata initial_data; 