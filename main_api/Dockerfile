# Use Python 3.10 on Bullseye
FROM python:3.10-bullseye

# Update and install required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libffi-dev libssl-dev

# Create and activate a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install project dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Give execute permissions to the init.sh file (if present)
RUN chmod +x init.sh

# Start your application (this could be your custom command or entry point)
# CMD ["./init.sh"]  # Uncomment if you have an init.sh script to run

