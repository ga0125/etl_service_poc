FROM python:3.9.5

# Allows for log messages to be immediately dumped to the stream instead of being buffered.
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt