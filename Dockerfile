FROM ubuntu:16.04

MAINTAINER jaggu4329 <jagadish.dachepalli@gmail.com>

RUN apt-get update && \
        apt-get install -y software-properties-common && \
        add-apt-repository ppa:jonathonf/python-3.6 && \
        apt-get update -y  && \
        apt-get install -y build-essential python3.6 python3.6-dev python3-pip && \
        apt-get install -y git  && \
        # update pip
        python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

COPY book-rental-calculator/ /book-rental-calculator


RUN python3.6 -m pip install -r /book-rental-calculator/requirements.txt

EXPOSE 80
EXPOSE 22
EXPOSE 5020
