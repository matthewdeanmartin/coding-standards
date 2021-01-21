Contributing
------------
Setup
```
# --skip-lock to speed up things
pipenv install --dev (--skip-lock)
# register pre-commit hooks if this is a git repo
pre-commit install
```

Build

The .gitlab-ci.yml file is for building remotely. Locally, do one of the following
```
./build.sh
# or run tools individually
isort . && black . && bandit . && flake8 && pre-commit run --all-files
# or run tools via pre-commit
pre-commit run --all-files
```



Build Script Documentation
--------------------------
Security features
- bandit
- detect-secrets (via pre-commit)
- .gitignore
- detect-aws-credentials via pre-commit
- detect-private-key via pre-commit

Quality Features
- flake8

Collaboration Features
- isort, black & .editorconfig so teams formatting is the same
- various minor generic format tools via pre-commit

## TODO
- flake8 & isort are double configured (setup.cfg and dotfiles)
- security
    - encourage .env usage for secrets
    - safety
    - gitsecrets (bash based)
- quality
    - pylint
    - sonar
    - mypy
    - others, but most benefit comes from pylint, sonar, mypy
- packaging
    - preferably with pyproject.toml on grounds that setup.py is a security hazard.
    - or setup.cfg only
    - or Dockerfile based
- tests
    - pytest
    - tox, vermin
    - coverage
- mutating
    - version bumping
    - upgrade to latest python
    - pypgrade, 2to3
- a default build script (although something that works for everyone will be hard)

