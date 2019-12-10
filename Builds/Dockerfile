FROM python:3.6.4

MAINTAINER jaggu4329 <jagadish.dachepalli@gmail.com>

COPY ../../book-rental-calculator/ /book-rental-calculator

RUN python -m virtualenv venv
RUN source venv/Scripts/activate
RUN python -m pip install -r requirements.txt
RUN source envs/dev

CMD [ "python", "./app.py" ]


