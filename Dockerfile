# Dockerfile

# pull the official docker image
FROM python:3.11-slim

# set work directory
WORKDIR /api_rest

RUN useradd appuser && chown appuser ./

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY  --chown=appuser requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY  --chown=appuser . .