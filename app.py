from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connexion à la base de données
def get_db_connection(testing=False):
    if testing:
        # Utiliser une base en mémoire pour les tests
        conn = sqlite3.connect(':memory:')
    else:
        conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn


# Fonction pour créer la base de données et la table des utilisateurs
def create_db(testing=False):
    if testing:
        # Utiliser une base en mémoire pour les tests
        conn = sqlite3.connect(':memory:')
    else:
        conn = sqlite3.connect('users.db')

    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
    ''')
    conn.commit()
    conn.close()


# Appeler la fonction create_db pour créer la base de données au démarrage de l'application
create_db()

# Page d'accueil (home)
@app.route('/home')
def home():
    return render_template('home.html')


# Page d'inscription (register)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vérification si l'utilisateur existe déjà
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        
        if user:
            return "Username already exists! Try a different one."
        
        # Enregistrement du nouvel utilisateur
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))  # Rediriger vers la page de connexion

    return render_template('register.html')

# Page de connexion (login)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()

        if user:
            return redirect(url_for('home'))  # Rediriger vers la page d'accueil
        else:
            return "Invalid credentials! Please try again."

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
