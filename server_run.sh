#!/bin/bash

cd testmeme
cd xmeme-backend
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8081