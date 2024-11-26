import whois
import json
from datetime import datetime

class WhoisTool:
    @staticmethod
    def parse_whois_data(domain):
        """
        Analyse les informations WHOIS d'un domaine
        
        Args:
            domain (str): Domaine à analyser
        
        Returns:
            dict: Informations structurées
        """
        try:
            # Requête WHOIS
            w = whois.whois(domain)
            
            # Conversion des dates
            def convert_date(date):
                if isinstance(date, list):
                    date = date[0] if date else None
                return date.strftime('%Y-%m-%d %H:%M:%S') if date else 'Non disponible'
            
            # Préparation des données
            whois_data = {
                'domain_name': w.domain_name[0] if isinstance(w.domain_name, list) else w.domain_name,
                'registrar': w.registrar,
                'creation_date': convert_date(w.creation_date),
                'expiration_date': convert_date(w.expiration_date),
                'name_servers': w.name_servers,
                'status': w.status if w.status else 'Statut non disponible',
                'emails': w.emails,
                'dnssec': w.dnssec,
                'name': w.name,
                'org': w.org,
                'country': w.country
            }
            
            return {
                'status': 'success',
                'data': whois_data
            }
        
        except whois.parser.PywhoisError as e:
            return {
                'status': 'error',
                'message': f'Erreur WHOIS : {str(e)}'
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Erreur inattendue : {str(e)}'
            }

    @staticmethod
    def save_whois_results(domain):
        """
        Sauvegarde les résultats WHOIS dans un fichier JSON
        
        Args:
            domain (str): Domaine à analyser
        
        Returns:
            str: Chemin du fichier sauvegardé
        """
        results = WhoisTool.parse_whois_data(domain)
        
        # Création du nom de fichier unique
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'whois_results_{domain.replace(".", "_")}_{timestamp}.json'
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=4)
        
        return filename

def test_whois_tool():
    """
    Fonction de test de l'outil WHOIS
    """
    # Domaines de test
    test_domains = [
        'google.com',
        'wikipedia.org', 
        'github.com'
    ]
    
    for domain in test_domains:
        print(f"\n--- Test WHOIS pour {domain} ---")
        result = WhoisTool.parse_whois_data(domain)
        
        if result['status'] == 'success':
            print("Informations du domaine :")
            for key, value in result['data'].items():
                print(f"{key}: {value}")
            
            # Sauvegarde automatique
            saved_file = WhoisTool.save_whois_results(domain)
            print(f"\nRésultats sauvegardés dans : {saved_file}")
        else:
            print(f"Erreur : {result['message']}")

# Exécution des tests si le script est lancé directement
if __name__ == '__main__':
    test_whois_tool()