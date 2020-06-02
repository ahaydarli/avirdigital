<!-- PROJECT SHIELDS -->
![Django CI](https://github.com/ahaydarli/avirdigital/workflows/Django%20CI/badge.svg?branch=master)
<!-- [![Build Status][build-shield]]() -->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="https://avirdigital.az/static/images/img/155.png" width="150" alt="Logo">

  <!-- <h3 align="center">Claking Tooling</h3> -->

  <p align="center">
    Avirdigital portfolio website
    <br />
    <br />
    <a href="https://example.com">Production</a>
    ·
    <a href="https://example.com">Staging</a>
  </p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Tests](#tests)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About

<p align="center">
  <img src="static/images/screenshot.png" width="500" alt="Logo">
</p>

### Built With
* [Python](https://python.org)
* [Django](https://docs.djangoproject.com/en/3.0/)


<!-- GETTING STARTED -->
## Getting Started with Development
This is a development setup guide for this project. Please follow the instructions to setup
project locally.

### 🤚 **Requirements**
- Python 3.7
- Pipenv ([installationinstallation guide](https://docs.pipenv.org/en/latest/install/#installing-pipenv)) or
- Poetry ([installationinstallation guide](https://python-poetry.org/docs/))

### ⏳ **Running locally**
- Pull the repo
- Create new pipenv environment (virtualenv)
    ```bash
    pipenv --python 3.7
  
  --for poetry
  
  poetry shell
    ```
- Install requirements
    ```bash
    pipenv install
  
  for poetry 
  
  poetry install
    ```
- To run on local
    ```bash
    pipenv shell
  
  --for poetry
  
  poetry shell
  
    python manage.py migrate
  
  python manage.py collectstatic
  
    python manage.py runserver
    ```

    Application will run on [127.0.0.1:8000](http://127.0.0.1:8000)

- For admin dashboard
    ```bash
    python manage.py createsuperuser
    python manage.py runserver
    ```

    Admin dashboard will run on [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Troubleshooting

<!-- Testing -->
## Testing
-  Django tests

    ```bash
    python manage.py test  
    ```
- Alternatively tox
    ```bash
    tox
    ```
<!-- CONTACT -->
## Contact


<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
