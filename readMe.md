#  Gestion d'Événements - Application Django

Une application web simple de gestion d’événements avec système d'authentification, CRUD complet, interface responsive et utilisation de Django côté back-end.

## Fonctionnalités

-  Inscription et authentification des utilisateurs
-  Création, modification, suppression et affichage d'événements
-  Tableau de bord avec résumé des événements
-  Interface propre et responsive avec Bootstrap
-  Protection des pages par connexion obligatoire

##  Technologies utilisées

- Python 3.13
- Django 5.2
- HTML5 / CSS3 (Bootstrap 5)
- SQLite (base de données par défaut)

## **Installation**

1. ## **Cloner le dépôt**

    - "git clone https://github.com/LLODIA221/gestion_evenements.git "
    - cd gestion-evenements

2. ## **Créer un environnement virtuel**
    - python -m venv venv
3. ## **Activer l'environnement virtuel**

## **Sur Windows :**

    .\venv\Scripts\activate

## **Sur macOS/Linux :**

    source venv/bin/activate

## 4.**Installer les dépendances**

    pip install -r requirements.txt

## 5.**Lancer les migrations**

    python manage.py makemigrations
    python manage.py migrate

## 6.**Créer un superutilisateur (admin)**

python manage.py createsuperuser

## 7.**Démarrer le serveur**
    python manage.py runserver
    Ouvre http://127.0.0.1:8000 dans le navigateur
