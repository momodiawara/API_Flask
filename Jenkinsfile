pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                // Vérifier les versions de Python et pip
                sh '''
                python3 --version
                pip --version
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                // Créer un environnement virtuel et installer les dépendances
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Application') {
            steps {
                // Lancer l'application Flask
                sh '''
                source venv/bin/activate
                FLASK_APP=app.py FLASK_ENV=production flask run --host=0.0.0.0 --port=5000 &
                '''
            }
        }
    }
    
    post {
        always {
            echo "Pipeline terminé."
        }
        success {
            echo "Application Flask déployée avec succès."
        }
        failure {
            echo "Le pipeline a échoué. Vérifiez les logs."
        }
    }
}
