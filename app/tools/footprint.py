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

def osint_search(domain):
    command = f"dnsrecon -d {domain}"
    return run_shell_command(command)

def wget_search(domain):
    command = f"wget {domain}"
    return run_shell_command(command)

def dig_search(query):
    command = f"dig {query}"
    return run_shell_command(command)

def nslookup_search(query):
    command = f"nslookup {query}"
    return run_shell_command(command)

@app.route('/footprint', methods=['POST'])
def footprint():
    domain = request.form.get('domain')
    tool = request.form.get('tool')
    
    if tool == 'whois':
        result = whois_search(domain)
    elif tool == 'osint':
        result = osint_search(domain)
    elif tool == 'wget':
        result = wget_search(domain)
    elif tool == 'dig':
        result = dig_search(domain)
    elif tool == 'nslookup':
        result = nslookup_search(domain)
    else:
        return jsonify({"status": "error", "message": "Invalid tool selected"})
    
    return jsonify({"status": "success", "data": result})

if __name__ == "__main__":
    app.run(debug=True)