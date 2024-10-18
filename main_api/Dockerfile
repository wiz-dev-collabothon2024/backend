FROM python:3.10.6-alpine3.16

RUN apk update && apk add --no-cache bash

# Install system dependencies
RUN apk add --no-cache build-base libffi-dev openssl-dev

# Create and activate a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install project dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Give execute permissions to the init.sh file
RUN chmod +x init.sh