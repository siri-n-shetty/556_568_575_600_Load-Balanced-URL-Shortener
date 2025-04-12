# Use official Python base image
FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# # Install system dependencies and Redis client dependencies
# RUN apt-get update && apt-get install -y \
#     gcc \
#     libffi-dev \
#     libssl-dev \
#     && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose Flask port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "main.py"]