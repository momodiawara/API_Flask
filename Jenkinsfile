pipeline {
    agent any

    environment {
        // Définir l'environnement virtuel
        VENV_DIR = '.venv'
    }

    stages {
        stage('Cloner le dépôt') {
            steps {
                // Cloner le dépôt via SSH
                git credentialsId: 'e17e6d7b-7c5f-457f-b0a0-ce096deb7983', url: 'git@github.com:momodiawara/API_Flask.git', branch: 'main'


            }
        }

        stage('Configurer l\'environnement virtuel') {
            steps {
                // Créer un environnement virtuel Python
                sh 'python3 -m venv .venv'

                // Activer l'environnement virtuel et installer les dépendances
                sh '''
                    .venv/bin/pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Exécuter les tests') {
            steps {
                // Exécuter les tests unitaires avec pytest (ou unittest si tu préfères)
                sh '.venv/bin/python3 -m unittest test_app.py'  // Utiliser pytest si tu préfères pytest
            }
        }

        stage('Nettoyage') {
            steps {
                // Supprimer l'environnement virtuel après les tests
                sh 'rm -rf .venv'
            }
        }
    }

    post {
        always {
            // Cette section est toujours exécutée après la fin du pipeline
            echo 'Pipeline terminé.'
        }
        success {
            echo 'Les tests ont réussi !'
        }
        failure {
            echo 'Les tests ont échoué. Vérifie les logs ci-dessus.'
        }
    }
}
