# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY .env /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY components /code/
COPY kamusy /code/
COPY ping /code/
COPY quickstart /code/
COPY utils /code/
COPY manage.py /code/
RUN pip install --upgrade pip
# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate
# RUN python3 manage.py importdb