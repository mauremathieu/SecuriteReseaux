from flask import Blueprint, render_template, request, jsonify
from app.tools.reconnaissance import get_domain_info
from app.tools.network_scan import ping_host, scan_network

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """Page d'accueil du framework"""
    return render_template('home.html', 
                           title='PyFlaSQL - Pentesting Framework',
                           description='Outils de reconnaissance et test de sécurité')

@main_bp.route('/reconnaissance', methods=['GET', 'POST'])
def recon_tools():
    """Page des outils de reconnaissance"""
    if request.method == 'POST':
        domain = request.form.get('domain')
        whois_results = get_domain_info(domain)
        return jsonify(whois_results)
    
    return render_template('reconnaissance.html')

@main_bp.route('/network-scan', methods=['GET', 'POST'])
def network_scanning():
    """Page de scan réseau"""
    if request.method == 'POST':
        target = request.form.get('target')
        scan_type = request.form.get('scan_type')
        
        if scan_type == 'ping':
            result = ping_host(target)
        elif scan_type == 'nmap':
            result = scan_network(target)
        
        return jsonify(result)
    
    return render_template('network_scan.html')