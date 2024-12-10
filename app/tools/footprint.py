from app.tools.run_shell_command import run_shell_command

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