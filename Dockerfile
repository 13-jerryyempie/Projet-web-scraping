# Utiliser une image Python complète au lieu de slim
FROM python:3.13

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .

# Mettre à jour les paquets et installer un compilateur C++ compatible
RUN apt-get update && apt-get install -y g++ build-essential cmake && apt-get clean

# Mettre à jour pip et installer les outils nécessaires
RUN pip install --upgrade pip setuptools wheel

# Installer numpy et pybind11 (dépendances possibles de chroma-hnswlib)
RUN pip install --no-cache-dir numpy pybind11

# Installer chroma-hnswlib après s’être assuré que l’environnement est prêt
RUN pip install --no-cache-dir --no-build-isolation chroma-hnswlib

# Installer les autres dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet
COPY . .

# Définir la commande de lancement de l'application
CMD ["python", "main.py"]
