# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run message_service.py when the container starts
CMD ["python", "message_service.py"]
