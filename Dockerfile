FROM ubuntu:20.04
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt-get install -y tzdata libcairo2-dev libsdl-pango-dev 
# pull official base image
FROM python:3.8.3

# set work directory
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CHANGE!
ENV APP_HOME=/root/test_dock
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR  $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
# copy project
COPY . $APP_HOME

# chown all the files to the app user
# RUN addgroup -S app && adduser -S app -G app
# RUN chown -R app:app $APP_HOME

# # change to the app user
# USER root

RUN pip install django gunicorn



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CHANGE!
# RUN chmod -R 664 /root/test_dock/static/
# RUN chmod -R 664 ./static
# EXPOSE 8000