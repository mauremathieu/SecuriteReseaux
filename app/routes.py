from flask import Flask, render_template, request, jsonify
from app.tools import reconnaissance, network_scan, enumeration

app = Flask(__name__)

@app.route('/')
def home():
    """Page d'accueil du framework"""
    return render_template('home.html', 
                           title='PyFlaSQL - Pentesting Framework',
                           description='Outils de reconnaissance et test de sécurité')

@app.route('/reconnaissance', methods=['GET', 'POST'])
def recon_tools():
    """Page des outils de reconnaissance"""
    if request.method == 'POST':
        # Logique de traitement des requêtes
        domain = request.form.get('domain')
        whois_results = reconnaissance.do_whois(domain)
        return jsonify(whois_results)
    
    return render_template('reconnaissance.html')

@app.route('/network-scan', methods=['GET', 'POST'])
def network_scanning():
    """Page de scan réseau"""
    if request.method == 'POST':
        target = request.form.get('target')
        scan_type = request.form.get('scan_type')
        
        if scan_type == 'ping':
            result = network_scan.ping_scan(target)
        elif scan_type == 'nmap':
            result = network_scan.nmap_scan(target)
        
        return jsonify(result)
    
    return render_template('network_scan.html')