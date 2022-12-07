FROM python:3.10-slim

RUN apt-get update && apt-get install -y git

RUN useradd -ms /bin/bash python

RUN pip install pipenv

USER python

WORKDIR /home/python/app

ENV PIPENV_VENV_IN_PROJECT=True

CMD ["./.docker/start_dev.sh"]