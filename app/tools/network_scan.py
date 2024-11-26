import os
import subprocess

def ping_host(host):
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        print(f"{host} is up!")
    else:
        print(f"{host} is down!")

def scan_network(network):
    result = subprocess.run(["nmap", "-sP", network], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    host = "8.8.8.8"  # Example host
    network = "192.168.1.0/24"  # Example network

    ping_host(host)
    scan_network(network)