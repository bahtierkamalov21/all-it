FROM python:latest

WORKDIR /usr/src/all-it

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set timezone
ENV TZ=Europe/Moscow

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8200
