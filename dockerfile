# Base Python image
FROM python:3.10-slim

# Working directory
WORKDIR /app

# System dependencies (safe for ML libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

# Expose Flask port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]