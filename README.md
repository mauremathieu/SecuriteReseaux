## Python Flask SQLite

This repository contains the code used for creating a Python-Flask-SQLite based environment for the cybersecurity ISMIN courses.

## Author
Maure Mathieu EI23
Cressant Fabien EI23

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies

##### Windows:
```zsh
pip install -r requirements.txt 
```

##### macOS/Linux:
```zsh
pip3 install -r requirements.txt
```

## Usage

##### Windows:
```zsh
python app.py
```
##### macOS/Linux:
```zsh
python3 app.py
```

## Description
This project sets up a web application using Python, Flask, and SQLite. It includes the following components:

- **app.py**: The main application file that initializes the Flask app and sets up the routes.
- **models.py**: Contains the database models and schema definitions using SQLAlchemy.
- **templates/**: Directory containing HTML templates for rendering web pages.
- **static/**: Directory for static files like CSS, JavaScript, and images.
- **requirements.txt**: Lists the Python dependencies needed to run the application.

The application demonstrates basic CRUD (Create, Read, Update, Delete) operations and user authentication mechanisms, which are essential for cybersecurity training in the ISMIN courses.

## Tools implemented









## Remerciements

Thank you, Raphael Vierra, for the courses.
https://gitlab.emse.fr/raphael.viera/pyflasql/-/tree/main/app?ref_type=heads