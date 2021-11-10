FROM python:3.8-alpine

RUN apk add gcc build-base linux-headers

RUN mkdir /web_memo
RUN mkdir /web_memo/templates
WORKDIR /web_memo

COPY requirements.txt ./
COPY app.py ./
COPY config.py ./
COPY make_db.py ./
COPY templates/ ./templates
COPY app.ini ./

RUN python make_db.py

RUN echo `pip --version`
RUN pip install -r requirements.txt

CMD [ "uwsgi","--ini","/web_memo/app.ini" ]