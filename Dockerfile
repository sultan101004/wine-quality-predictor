# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt .

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ ./app/

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]
