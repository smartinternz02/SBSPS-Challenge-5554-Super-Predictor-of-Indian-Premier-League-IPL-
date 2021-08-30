FROM python:3.8.2-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk --update add python liberty-for-java py-pip openssl ca-certificates py-openssl wget bash linux-headers
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev liberty-for-java python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install --upgrade pipenv\
  && pip install --upgrade -r /app/requirements.txt\
  && apk del build-dependencies

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "hello.py" ]