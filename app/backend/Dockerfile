# set the base image 
FROM python:3.8.2

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN chmod g+rwx /code/logs

RUN pip install -U pip
RUN pip install -Ur requirements.txt

EXPOSE 5000

CMD python manage.py collectstatic --no-input; python manage.py migrate; gunicorn arm.wsgi -b 0.0.0.0:5000 --log-level debug
