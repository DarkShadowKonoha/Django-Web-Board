# A Complete Beginner's Guide to Django

[![Python Version](https://img.shields.io/badge/python-3.8.0-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.1.2-brightgreen.svg)](https://djangoproject.com)


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:sibtc/django-beginners-guide.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Setup the local configurations:

```bash
cp .env.example .env
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

