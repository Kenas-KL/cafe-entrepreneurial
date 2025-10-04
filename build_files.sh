#!/bin/bash
# build_files.sh

# Installer les dépendances Python
python -m pip install --upgrade pip
pip install -r requirements.txt

# Construire Tailwind
python manage.py tailwind build

# Collecter les fichiers statiques
python manage.py collectstatic --noinput
