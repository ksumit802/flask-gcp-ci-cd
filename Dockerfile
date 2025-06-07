# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install Flask
RUN pip install flask

# Expose port 8080 to the outside
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]
