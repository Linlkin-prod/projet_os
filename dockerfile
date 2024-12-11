# Utilise une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier serveur dans le conteneur
COPY server.py .

# Exposer le port pour le serveur TCP
EXPOSE 12345

# Commande à exécuter lors du lancement du conteneur
CMD ["python", "server.py"]
