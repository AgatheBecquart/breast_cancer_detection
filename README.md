# Détection de tumeurs mammaires avec YOLO

Ce projet est une application de détection de tumeurs mammaires basée sur le modèle YOLO (You Only Look Once). Il permet aux radiologues de charger des images radiographiques et de détecter automatiquement la présence de tumeurs du sein.

L'application utilise le modèle YOLOv8 pour la détection d'objets et est développée en utilisant la bibliothèque Streamlit pour créer une interface utilisateur conviviale.

## Prérequis

- Python 3.7 ou une version supérieure
- Les packages requis sont répertoriés dans le fichier `requirements.txt`

## Installation

1. Clonez ce dépôt de code :

    https://github.com/AgatheBecquart/breast_cancer_detection.git

2. Accédez au répertoire du projet :

    cd breast_cancer_detection

3. Installez les dépendances :

    pip install -r requirements.txt


## Utilisation

1. Lancez l'application Streamlit :

    streamlit run app.py


2. Ouvrez votre navigateur et accédez à l'URL `http://localhost:8501` pour utiliser l'application.

3. Chargez une image radiographique à partir de l'interface de l'application.

4. Cliquez sur le bouton "Détecter les tumeurs" pour exécuter la détection de tumeurs sur l'image chargée.

5. Les résultats de la détection, y compris les images avec les tumeurs détectées, seront affichés dans l'interface de l'application.

## Auteur

[Jonathan Impe](https://github.com/impejonathan)
[Agathe Becquart](https://github.com/AgatheBecquart)

## Ressources supplémentaires

- [YOLOv8](https://github.com/ultralytics/yolov8)
- [Streamlit](https://streamlit.io/)