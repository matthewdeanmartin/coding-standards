#!/usr/bin/env bash
isort . && black . && bandit -r . && flake8 && pre-commit run --all-files
