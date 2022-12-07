#!/bin/bash

pipenv install --dev
pipenv run pre-commit install
pipenv run python manage.py migrate

tail -f /dev/null
