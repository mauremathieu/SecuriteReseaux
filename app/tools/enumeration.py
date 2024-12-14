from app.tools.run_shell_command import run_shell_command

def banner_grabbing(target):
    command = f"nmap -sV {target}"
    return run_shell_command(command)

def os_enumeration(target):
    command = f"nmap -O {target}"
    return run_shell_command(command)

def user_enumeration(target):
    command = f"nmap --script smb-enum-users {target}"
    return run_shell_command(command)
