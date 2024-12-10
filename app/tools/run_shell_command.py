import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {"command": command, "output": result.stdout, "error": result.stderr}
    except Exception as e:
        return {"command": command, "error": str(e)}