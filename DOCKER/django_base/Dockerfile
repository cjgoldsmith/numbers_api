FROM python:3.9.0-buster
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y && apt-get autoclean -y

RUN pip install --upgrade pip

RUN mkdir -p /code
WORKDIR /code

ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt