FROM python:3.5

WORKDIR /app

COPY requirements.txt requirements-dev.txt /app/
RUN pip install -r requirements-dev.txt

COPY goclub /app

EXPOSE 8000
