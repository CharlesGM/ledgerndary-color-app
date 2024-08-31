# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the environment variable for the page colour
# You can change the colour here, e.g., PAGE_COLOUR=blue
ENV PAGE_COLOUR=brown

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Flask and any other required packages
RUN pip install --no-cache-dir flask

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable for the Python path
ENV PYTHONPATH=/usr/src/app

# Run app.py when the container launches
CMD ["python", "app.py"]