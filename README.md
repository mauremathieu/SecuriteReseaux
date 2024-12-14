## Python Flask SQLite

This repository contains the code used for creating a Python-Flask-SQLite based environment for the cybersecurity ISMIN courses.

## Author
Maure Mathieu EI23
Cressant Fabien EI23

## Installation and usage

##### Linux:
```zsh
chmod +x install_packages.sh
./install_packages.sh
python3 run.py
```

## Description
This project sets up a web application using Python, Flask, and SQLite. It includes the following components:

- **run.py**: The main application file that initializes the Flask app and sets up the routes.
- **app/templates/**: Directory containing HTML templates for rendering web pages.
- **app/tools/**: Directory containing python tools.
- **requirements.txt**: Lists the dependencies needed to run the application.

## Tools implemented
- **Footprinting**: WHOIS, OSINT, Wget, Dig, Nslookup
- **Network Scanning**: Ping, Nmap
- **Enumeration**: Banner Grabbing, OS Enumeration, User Enumeration
- **Gaining Access**: Metasploit, FTP Exploit, SSH Exploit
- **Account**: Flask-SQLAlchemy, Flask-Login

## Remerciements

Thank you, Raphael Vierra, for the courses.
[Application inspired from](https://gitlab.emse.fr/raphael.viera/pyflasql/-/tree/main/app?ref_type=heads)