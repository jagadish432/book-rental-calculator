FROM ubuntu:18.04

MAINTAINER jaggu4329 <jagadish.dachepalli@gmail.com>

RUN apt-get update && \
        apt-get install -y --no-install-recommends python3 python3-virtualenv && apt-get install curl -y && apt-get install vim -y
		
		
ENV virtual_env=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $virtual_env

ENV PATH="$virtual_env/bin:$PATH"


COPY book-rental-calculator/ /book-rental-calculator

ENV FLASK_APP app

RUN pip install -r /book-rental-calculator/requirements.txt

EXPOSE 5020

WORKDIR /book-rental-calculator/

CMD ["sh", "dev.sh"]


