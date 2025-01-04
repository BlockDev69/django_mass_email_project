# 🚀Mass emailing with django_celery

## About
  The django project simply aims to send a single email to several addresses, with the option of attaching a document.

## requirements
To successfully run this project, you need to have the following software installed on your machine:
- Docker: Ensure Docker is installed and running. Visit Docker's official website for installation instructions.

- Docker Compose: Make sure Docker Compose is installed. It usually comes with Docker, but you can download it separately from here.

- Python 3.8 or higher: Although Python is managed within the Docker containers, having it installed is useful for local development and script execution.

- git: For cloning the repository and version control. Install it from here if you don't have it.

### Installation Steps
1. Clone the Repository
```console
git clone https://github.com/BlockDev69/django_mass_email_project.git
cd django_mass_email_project
```
2. Start the Services with Docker Compose
```console
docker-compose up -d
```
3. Access the Application

- The Django application will be available at http://localhost:8000.

- Celery workers and RabbitMQ are configured through the Docker compose file.

### Additional Notes
#### RabbitMQ Management Interface

- Access the RabbitMQ management dashboard at http://localhost:15672.

- Default credentials: guest / guest.

# Use
  - Create account
  - In the /reviews page, enter the required information in the required information form:
  
        1. Name
        2. Email: Here you enter the various e-mail addresses line by line.
        3. Your review
        4. File: Here you can choose whether to send an attachment or not, the document must have a maximum size of 5MB.

# 🎉Contribution 

All ideas and contributions are welcome and will be analyzed and responded to as soon as possible.
So don't hesitate.😁