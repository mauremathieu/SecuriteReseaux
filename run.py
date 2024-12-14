from app import create_app
from config import Config  

app = create_app(Config)

if __name__ == '__main__':
    # Mode debug pour le développement
    app.run(
        host='0.0.0.0',  # Accessible sur tous les réseaux
        port=5000,       # Port standard Flask
        debug=True       # Mode développement
    )