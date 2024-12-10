from app.tools.run_shell_command import run_shell_command

def ping_host(host):
    command = f"ping -c 1 {host}"
    return run_shell_command(command)

def scan_network(network):
    command = f"nmap -sP {network}"
    return run_shell_command(command)
