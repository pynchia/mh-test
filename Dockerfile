# FROM python:3.8-alpine
FROM python:3-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install -e .
RUN pytest -s --cov=mh/
