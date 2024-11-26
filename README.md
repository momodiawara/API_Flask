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
|-- test.py              # Fichier de test unitaire
|-- templates/           # HTML pour les pages (home, login, register)
|   |-- home.html
|   |-- login.html
|   |-- register.html
|-- static/              # Fichiers CSS, JS (optionnel)
|-- requirements.txt     # Dépendances du projet
|-- Jenkinsfile          # Pipeline Jenkins
|-- Dockerfile           # Pipeline docker
|-- README.md            # Documentation du projet

Dépendances

Les dépendances sont listées dans requirements.txt. Exemple :

Flask==2.2.3

Fonctionnalités

    Page d'accueil : Liens pour s'inscrire ou se connecter.
    Connexion : Formulaire pour se connecter avec un email et un mot de passe.
    Inscription : Formulaire pour créer un nouveau compte.
    Base de données SQLite3 : Stockage des utilisateurs enregistrés.


Lancer Jenkins avec Docker

Vous pouvez utiliser Docker pour exécuter Jenkins facilement.
1. Prérequis

    Docker doit être installé sur votre machine. Guide d'installation Docker

2. Tirer l'image officielle de Jenkins

Téléchargez l'image Docker officielle de Jenkins LTS (Long Term Support) :

docker pull jenkins/jenkins:lts

3. Lancer Jenkins avec Docker

Exécutez la commande suivante pour créer et lancer un conteneur Jenkins :

docker run -d -p 8080:8080 -p 50000:50000 --name jenkins \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

Explications :

    -d : Exécute le conteneur en arrière-plan.
    -p 8080:8080 : Expose l'interface web Jenkins sur le port 8080.
    -p 50000:50000 : Expose le port pour les agents Jenkins distants.
    --name jenkins : Nomme le conteneur jenkins.
    -v jenkins_home:/var/jenkins_home : Monte un volume pour la persistance des données.

4. Accéder à Jenkins

    Ouvrez votre navigateur et accédez à :
    http://localhost:8080
    Obtenez le mot de passe initial en consultant les logs du conteneur Docker :

docker logs jenkins

Recherchez une ligne contenant :
Please use the following password to proceed to installation
Copiez ce mot de passe et connectez-vous.
5. Arrêter ou redémarrer Jenkins

    Arrêter Jenkins :

docker stop jenkins

Redémarrer Jenkins :

    docker start jenkins

6. Supprimer Jenkins

Pour supprimer le conteneur Jenkins et ses données, utilisez la commande suivante :

docker rm -f jenkins
docker volume rm jenkins_home

7. Monter un répertoire local (Optionnel)

Pour conserver les données sur votre machine locale, montez un répertoire avec cette commande :

docker run -d -p 8080:8080 -p 50000:50000 --name jenkins \
  -v $(pwd)/jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

Les données seront stockées dans le dossier jenkins_home dans votre répertoire actuel.

Tests

Pour exécuter des tests (si configuré avec Pytest) :

pytest

Auteurs

    DIAWARA Mohamed
    Contact : md2832845@gmail.com
