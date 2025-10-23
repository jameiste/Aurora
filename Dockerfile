# Dockerfile
FROM python:3.11-slim

# System basics
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


# Copy code
COPY . /app

# Run
CMD ["python", "main.py"]
