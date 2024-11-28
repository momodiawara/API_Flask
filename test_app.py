import unittest
import sqlite3
from app import app, create_db, get_db_connection  # Importation de l'application et de la fonction de création de la DB

class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Cette méthode est appelée une fois avant tous les tests."""
        create_db(testing=True)  # Créer la base de données en mémoire avant les tests
        cls.app = app.test_client()  # Créer un client de test pour l'application
        cls.app.testing = True  # Passer l'application en mode test

    def setUp(self):
        """Cette méthode est appelée avant chaque test."""
        self.conn = get_db_connection()  # Connexion à la base de données en mémoire
        self.cursor = self.conn.cursor()  # Créer un curseur pour manipuler la base de données
        self.cursor.execute("DELETE FROM users")  # Supprimer les utilisateurs avant chaque test
        self.conn.commit()

    def tearDown(self):
        """Cette méthode est appelée après chaque test."""
        self.conn.close()  # Fermer la connexion à la base de données après chaque test

    def test_database_setup(self):
        """Vérifier si la table 'users' existe dans la base de données"""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)  # La table 'users' doit exister

    def test_register_user(self):
        """Tester l'inscription d'un nouvel utilisateur"""
        response = self.app.post('/register', data=dict(username='testuser', password='password'), follow_redirects=False)
        self.assertEqual(response.status_code, 302)  # Redirection après inscription

        # Vérifier que l'utilisateur a bien été ajouté dans la base de données
        self.cursor.execute("SELECT * FROM users WHERE username = 'testuser'")
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)  # L'utilisateur doit exister dans la base de données

    def test_login_user(self):
        """Tester la connexion d'un utilisateur"""
        # Ajouter un utilisateur de test dans la base de données
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('testuser', 'password'))
        self.conn.commit()

        # Essayer de se connecter avec les bonnes informations d'identification
        response = self.app.post('/', data=dict(username='testuser', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)  # Connexion réussie

        # Essayer de se connecter avec des informations d'identification incorrectes
        response = self.app.post('/', data=dict(username='wronguser', password='wrongpassword'), follow_redirects=True)
        self.assertIn(b"Invalid credentials! Please try again.", response.data)  # Vérifier le message d'erreur

    def test_home(self):
        """Tester la page d'accueil"""
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200)  # Vérifier que la page d'accueil se charge correctement


    
if __name__ == '__main__':
    unittest.main()
