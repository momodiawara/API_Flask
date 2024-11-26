# Flask Application with Jenkins Pipeline
simple docker example

Description

Cette application est une petite démonstration d'un site web Flask avec des fonctionnalités de connexion, d'inscription, et une page d'accueil. Elle est automatisée avec Jenkins pour l'installation, l'exécution et le déploiement.

Installation
1. Clonez le projet

git clone <url-de-votre-depot>
cd <nom-du-projet>

2. Créez un environnement virtuel

   python3 -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate

3. Installez les dépendances

   pip install -r requirements.txt
   
4. Créez la base de données

   python app.py create_db

Utilisation

Lancer l'application localement

python app.py

Par défaut, l'application s'exécute sur http://127.0.0.1:5000

Voici un exemple de fichier README.md pour votre projet Flask intégré avec Jenkins :
Flask Application with Jenkins Pipeline
Description

Cette application est une petite démonstration d'un site web Flask avec des fonctionnalités de connexion, d'inscription, et une page d'accueil. Elle est automatisée avec Jenkins pour l'installation, l'exécution et le déploiement.
Installation
1. Clonez le projet

git clone <url-de-votre-depot>
cd <nom-du-projet>

2. Créez un environnement virtuel

python3 -m venv venv
source venv/bin/activate  # Sous Windows : venv\Scripts\activate

3. Installez les dépendances

pip install -r requirements.txt

4. Créez la base de données

python app.py create_db

Utilisation
Lancer l'application localement

python app.py

Par défaut, l'application s'exécute sur http://127.0.0.1:5000.
Jenkins Pipeline
Étapes d'intégration avec Jenkins

    Configuration Jenkins :
        Installez Jenkins sur votre machine.
        Ajoutez un nouveau job Jenkins avec Pipeline comme type de projet.

    Jenkinsfile :
        Le pipeline est décrit dans le fichier Jenkinsfile à la racine du projet.
        Jenkins exécutera les étapes suivantes :
            Création d'un environnement virtuel.
            Installation des dépendances (pip install).
            Lancement de l'application Flask.

    Commandes utilisées dans Jenkins :
        Activation de l'environnement virtuel :

source venv/bin/activate

Installation des dépendances :

pip install -r requirements.txt

Exécution de Flask :

        FLASK_APP=app.py FLASK_ENV=production flask run --host=0.0.0.0 --port=5000

Structure du projet

|-- app.py               # Fichier principal de l'application Flask
|-- templates/           # HTML pour les pages (home, login, register)
|   |-- home.html
|   |-- login.html
|   |-- register.html
|-- static/              # Fichiers CSS, JS (optionnel)
|-- requirements.txt     # Dépendances du projet
|-- Jenkinsfile          # Pipeline Jenkins
|-- README.md            # Documentation du projet

Dépendances

Les dépendances sont listées dans requirements.txt. Exemple :

Flask==2.2.3

Fonctionnalités

    Page d'accueil : Liens pour s'inscrire ou se connecter.
    Connexion : Formulaire pour se connecter avec un email et un mot de passe.
    Inscription : Formulaire pour créer un nouveau compte.
    Base de données SQLite3 : Stockage des utilisateurs enregistrés.

Tests

Pour exécuter des tests (si configuré avec Pytest) :

pytest

Auteurs

    DIAWARA Mohamed
    Contact : md2832845@gmail.com
