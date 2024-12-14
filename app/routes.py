from flask import Blueprint, render_template, request, jsonify
from app.tools.footprint import whois_search, osint_search, wget_search, dig_search, nslookup_search
from app.tools.network_scan import ping_host, scan_network
from app.tools.enumeration import banner_grabbing, os_enumeration, user_enumeration
from app.tools.gaining_access import metasploit_exploit, ftp_exploit, ssh_exploit

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
            results = whois_search(domain)
        elif tool == 'osint':
            results = osint_search(domain)
        elif tool == 'wget':
            results = wget_search(domain)
        elif tool == 'dig':
            results = dig_search(domain)
        elif tool == 'nslookup':
            results = nslookup_search(domain)
        else:
            results = {"status": "error", "message": "Invalid tool selected"}
        
        return jsonify({"status": "success", "data": results})
    
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
        
        return jsonify({"status": "success", "data": result})
    
    return render_template('network_scan.html')

@main_bp.route('/enumeration', methods=['GET', 'POST'])
def enumeration_tools():
    """Enumeration tools page"""
    if request.method == 'POST':
        target = request.form.get('target')
        tool = request.form.get('tool')
        
        if tool == 'banner':
            result = banner_grabbing(target)
        elif tool == 'os':
            result = os_enumeration(target)
        elif tool == 'user':
            result = user_enumeration(target)
        else:
            result = {"status": "error", "message": "Invalid tool selected"}
        
        return jsonify({"status": "success", "data": result})
    
    return render_template('enumeration.html')

@main_bp.route('/gaining-access', methods=['GET', 'POST'])
def gaining_access_tools():
    """Gaining access tools page"""
    if request.method == 'POST':
        target = request.form.get('target')
        tool = request.form.get('tool')
        
        if tool == 'metasploit':
            result = metasploit_exploit(target)
        elif tool == 'ftp':
            result = ftp_exploit(target)
        elif tool == 'ssh':
            result = ssh_exploit(target)
        else:
            result = {"status": "error", "message": "Invalid tool selected"}
        
        return jsonify({"status": "success", "data": result})
    
    return render_template('gainingAccess.html')

@main_bp.route('/gaining-access/metasploit', methods=['POST'])
def metasploit_access():
    target = request.form.get('target')
    result = metasploit_exploit(target)
    return jsonify({"status": "success", "data": result})

@main_bp.route('/gaining-access/ftp', methods=['POST'])
def ftp_access():
    target = request.form.get('target')
    result = ftp_exploit(target)
    return jsonify({"status": "success", "data": result})

@main_bp.route('/gaining-access/ssh', methods=['POST'])
def ssh_access():
    target = request.form.get('target')
    result = ssh_exploit(target)
    return jsonify({"status": "success", "data": result})