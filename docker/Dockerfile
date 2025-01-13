# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (change this based on your service)
EXPOSE 5000

# Set the entrypoint (change this based on your service)
CMD ["python", "message-service/publisher.py"]  # or replace with other service entry point
