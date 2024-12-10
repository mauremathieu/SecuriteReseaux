import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'votre_cle_secrete'
    DEBUG = True
    
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
        }
    }

class DevelopmentConfig(Config):
    DEVELOPMENT = True

class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False