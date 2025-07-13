# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything from root (../) into /app
COPY .. .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
