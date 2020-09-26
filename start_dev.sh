#!/bin/bash
echo "-----Abhyasa App-----"
echo "Creating virtual environment..."
python -m venv env

echo "Activating virtual environment..."
source env/bin/activate
echo "---------------------------------"

echo "Installing Dependencies..."
python -m pip install -r requirements-dev.txt

echo "---------------------------------"
echo "Starting App..."
export FLASK_APP=run.py
export FLASK_ENV=development

FLASK_DEBUG=1 && python -m flask run --port 8085