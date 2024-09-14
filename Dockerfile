# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder into the container at /app
COPY app/ /app/

# Expose the port Flask runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "api.py"]
