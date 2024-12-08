import whois
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {"command": command, "output": result.stdout, "error": result.stderr}
    except Exception as e:
        return {"command": command, "error": str(e)}
    
def whois_search(domain):
    command = f"whois {domain}"
    return run_shell_command(command)

def osint_search(query):
    command = f"some_osint_tool {query}"
    return run_shell_command(command)

def phishing_check(domain):
    command = f"some_phishing_tool {domain}"
    return run_shell_command(command)

def mantego_search(query):
    command = f"some_mantego_tool {query}"
    return run_shell_command(command)

def recon_ng_search(query):
    command = f"some_recon_ng_tool {query}"
    return run_shell_command(command)

def shodan_search(query):
    command = f"some_shodan_tool {query}"
    return run_shell_command(command)

@app.route('/footprint', methods=['POST'])
def footprint():
    domain = request.form.get('domain')
    tool = request.form.get('tool')
    
    if tool == 'whois':
        result = whois_search(domain)
    elif tool == 'osint':
        result = osint_search(domain)
    elif tool == 'phishing':
        result = phishing_check(domain)
    elif tool == 'mantego':
        result = mantego_search(domain)
    elif tool == 'recon-ng':
        result = recon_ng_search(domain)
    elif tool == 'shodan':
        result = shodan_search(domain)
    else:
        return jsonify({"status": "error", "message": "Invalid tool selected"})
    
    return jsonify({"status": "success", "data": result})

if __name__ == "__main__":
    app.run(debug=True)