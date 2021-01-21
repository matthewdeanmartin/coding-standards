Cookiecutters
-------------

Installing cookiecutter. Consider using pipx to globally install cookie cutter
because you will need this before your virtual environment has been created.
```
pipx install cookiecutter
```

After cloning the coding-standards repo, run
```
cookiecutter /c/Users/johndoe/GitHub/coding-standards/cookiecutters/pipenv/
# or
cookiecutter /c/Users/johndoe/GitHub/coding-standards/cookiecutters/poetry/
# or
cookiecutter /c/Users/johndoe/GitHub/coding-standards/cookiecutters/django/
# etc
```

Answer questions and then you have a standards compliant starting point

- `django` is coding standards compliance version of the default django skeleton
- `pipenv` is a project for deployment by git clone & `pipenv sync` to install the exact dependencies
- `poetry` is a project for deployment via packaging or `poetry install`
- `requirements_txt` is for a project packaged with setup.py and deployed with pip
