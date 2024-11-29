import subprocess

def nmap_scan(target):
    """Perform an nmap scan to grab banner, OS, and user information."""
    try:
        result = subprocess.run(['nmap', '-A', target], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
