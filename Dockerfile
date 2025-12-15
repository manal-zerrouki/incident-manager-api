# 1) Image de base Python
FROM python:3.10-slim

# 2) Répertoire de travail dans le conteneur
WORKDIR /app

# 3) Copier les fichiers de l'application
COPY requirements.txt .

# 4) Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copier tout le projet dans le conteneur
COPY . .

# 6) Exposer le port FastAPI
EXPOSE 8000

# 7) Lancer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
