FROM python:3.8-slim-buster

ENV FLASK_APP Server.py

RUN python3.8 -m pip install flask
COPY . ./src/

WORKDIR /src

EXPOSE 5000/tcp

ENTRYPOINT python3.8 -m flask run --host=0.0.0.0
