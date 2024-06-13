# Use python 3.10.12 as the base image
FROM python:3.10.12

# Avoiding user interaction with tzdata
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    git \
    lynx \
    && rm -rf /var/lib/apt/lists/*
    
# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

# Expose the port Hugo runs on
EXPOSE 8000

# Set the command to start Hugo server
# CMD ["python", "app/main.py"]