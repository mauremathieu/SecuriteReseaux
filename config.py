import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuration des outils
    TOOLS_CONFIG = {
        'nmap': {
            'enabled': True,
            'default_params': ['-sn']  # Scan de ping par défaut
        },
        'whois': {
            'enabled': True
        },
        'shodan': {
            'enabled': False,  # Nécessite une clé API
            'api_key': os.environ.get('SHODAN_API_KEY')
        },
        'dnsrecon': {
            'enabled': True
        },
        'wget': {
            'enabled': True
        },
        'dig': {
            'enabled': True
        },
        'nslookup': {
            'enabled': True
        },
        'metasploit': {
            'enabled': True
        },
        'ftp': {
            'enabled': True
        },
        'ssh': {
            'enabled': True
        }
    }

class DevelopmentConfig(Config):
    DEVELOPMENT = True

class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = False