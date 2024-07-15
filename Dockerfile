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

# Set environment variables for Django settings and superuser creation
ENV DJANGO_SETTINGS_MODULE=alumni.settings
ENV DJANGO_SUPERUSER_FIRST_NAME="Oleg"
ENV DJANGO_SUPERUSER_LAST_NAME="Milashkin"
ENV DJANGO_SUPERUSER_EMAIL="student@innopolis.university"
ENV DJANGO_SUPERUSER_PASSWORD="admin"

# Collect static files
RUN python alumni/manage.py collectstatic --noinput

# Make migrations and migrate the database
RUN python alumni/manage.py makemigrations --noinput && \
    python alumni/manage.py migrate --noinput

# Create superuser
RUN python manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL --first_name $DJANGO_SUPERUSER_FIRST_NAME --last_name $DJANGO_SUPERUSER_LAST_NAME

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "alumni/manage.py", "runserver", "0.0.0.0:8000"]