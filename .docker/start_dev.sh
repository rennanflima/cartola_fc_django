#!/bin/bash

pipenv install --dev
pipenv run python manage.py migrate

tail -f /dev/null