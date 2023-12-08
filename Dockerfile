# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install system dependencies including ffmpeg
RUN apt-get update \
    && apt-get install -y libssl-dev libffi-dev ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and switch to it
RUN useradd -m myuser
USER myuser

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
