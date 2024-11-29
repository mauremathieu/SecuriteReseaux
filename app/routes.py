from flask import Blueprint, render_template, request, jsonify
from app.tools.footprint import get_domain_info, osint_search, phishing_check, mantego_search, recon_ng_search, shodan_search
from app.tools.network_scan import ping_host, scan_network
from app.tools.enumeration import nmap_scan
from app.tools.gainingAccess import metasploit_exploit, ftp_exploit, ssh_exploit

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """Home page of the framework"""
    return render_template('home.html', 
                           title='PyFlaSQL - Pentesting Framework',
                           description='Reconnaissance and security testing tools')

@main_bp.route('/footprint', methods=['GET', 'POST'])
def footprint_tools():
    """Footprint tools page"""
    if request.method == 'POST':
        domain = request.form.get('domain')
        tool = request.form.get('tool')
        
        if tool == 'whois':
            results = get_domain_info(domain)
        elif tool == 'osint':
            results = osint_search(domain)
        elif tool == 'phishing':
            results = phishing_check(domain)
        elif tool == 'mantego':
            results = mantego_search(domain)
        elif tool == 'recon-ng':
            results = recon_ng_search(domain)
        elif tool == 'shodan':
            results = shodan_search(domain)
        else:
            results = {"status": "error", "message": "Invalid tool selected"}
        
        return jsonify(results)
    
    return render_template('footprint.html')

@main_bp.route('/network-scan', methods=['GET', 'POST'])
def network_scanning():
    """Network scan page"""
    if request.method == 'POST':
        target = request.form.get('target')
        scan_type = request.form.get('scan_type')
        
        if scan_type == 'ping':
            result = ping_host(target)
        elif scan_type == 'nmap':
            result = scan_network(target)
        
        return jsonify(result)
    
    return render_template('network_scan.html')

@main_bp.route('/enumeration', methods=['GET', 'POST'])
def enumeration_tools():
    """Enumeration tools page"""
    if request.method == 'POST':
        target = request.form.get('target')
        result = nmap_scan(target)
        return jsonify({"status": "success", "results": result})
    
    return render_template('enumeration.html')

@main_bp.route('/gaining-access', methods=['GET', 'POST'])
def gaining_access_tools():
    """Gaining access tools page"""
    if request.method == 'POST':
        target = request.form.get('target')
        # Add logic for gaining access tools here
        # result = gaining_access_tool(target)
        result = {"status": "success", "results": "Gaining access results for " + target}
        return jsonify(result)
    
    return render_template('gainingAccess.html')

@main_bp.route('/gaining-access/metasploit', methods=['POST'])
def metasploit_access():
    target = request.form.get('target')
    result = metasploit_exploit(target)
    return jsonify(result)

@main_bp.route('/gaining-access/ftp', methods=['POST'])
def ftp_access():
    target = request.form.get('target')
    result = ftp_exploit(target)
    return jsonify(result)

@main_bp.route('/gaining-access/ssh', methods=['POST'])
def ssh_access():
    target = request.form.get('target')
    result = ssh_exploit(target)
    return jsonify(result)