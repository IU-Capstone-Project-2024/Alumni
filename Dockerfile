# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Set environment variables
ENV EMAIL_HOST=${EMAIL_HOST}
ENV EMAIL_HOST_USER=${EMAIL_HOST_USER}
ENV EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD}
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

# Collect static files
RUN python alumni/manage.py collectstatic --noinput

# Make migrations and migrate the database
RUN python alumni/manage.py makemigrations --noinput && \
    python alumni/manage.py migrate --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]