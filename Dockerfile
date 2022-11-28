FROM python:3.9-slim

ARG DISCORD_TOKEN
ARG RIOT_API_TOKEN

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV DISCORD_TOKEN = $DISCORD_TOKEN
ENV RIOT_API_TOKEN = $RIOT_API_TOKEN

COPY . .
CMD [ "python", "app.py"]
