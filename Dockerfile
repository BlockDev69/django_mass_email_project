# Image de base Python
FROM python:3.11

# Répertoire de travail
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copie du reste du code
COPY . /code/

EXPOSE 8000

# Commande de démarrage par défaut
CMD ["python", "manage.py", "runserver", "0.0.0.0.8000"]