#!/bin/bash
# python -m venv env
# source env/bin/activate

poetry shell
poetry install

export FLASK_APP=run.py
export FLASK_ENV=development

flask run --port 8085