# set base image (host OS)
FROM python:3.9-slim as builder
# set the working directory in the container

FROM builder AS build1

RUN update-ca-certificates

WORKDIR /code
# copy the dependencies file to the working directory

VOLUME my-volume:/code

FROM builder as build2

COPY requirements.txt .

# install dependencies
RUN mkdir /data && \
    pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
ENV FLASK_ENV development

RUN pip install --upgrade pip && pip install mysql-connector-python

# command to run on container start
CMD [ "python", "./chatApp.py" ]

# copy the content of the local src directory to the working directory
COPY . .
