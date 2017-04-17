#!/bin/sh

run:
	python manage.py runserver

test:
	python manage.py test

requirements:
	pip install -r requirements.txt

migrate:
	python manage.py migrate