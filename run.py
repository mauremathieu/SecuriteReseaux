from app import create_app
from config import Config  # Assuming you have a config.py file with a Config class

# Créer l'instance de l'application
app = create_app(Config)

if __name__ == '__main__':
    # Mode debug pour le développement
    app.run(
        host='0.0.0.0',  # Accessible sur tous les réseaux
        port=5000,       # Port standard Flask
        debug=True       # Mode développement
    )