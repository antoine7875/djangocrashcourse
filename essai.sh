#!/bin/bash

#redémarrage bdd
rm -f tmp.db db.sqlite3
rm -r ant1/migrations
python manage.py makemigrations
python manage.py migrate
