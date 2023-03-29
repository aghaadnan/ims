# Use an official Python runtime as a parent image
#FROM python:3.8-slim-buster
FROM python:3.6-slim
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 8000 for the Django app to listen on
EXPOSE 8000

# Define environment variables
ENV DJANGO_SETTINGS_MODULE=IMS.settings
ENV PYTHONUNBUFFERED=1
#RUN chmod +x entrypoint.sh

# Set up the entrypoint for the container
#ENTRYPOINT ["./entrypoint.sh"]

# Use CMD to specify the default command to run when a container is started
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
