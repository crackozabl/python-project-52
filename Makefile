init:
	poetry install

l10n:
	poetry run manage.py makemessages -l ru -e html,txt,py
	poetry run manage.py compilemessages

db:
	poetry run manage.py migrate

setup: init l10n db

PORT ?= 8000
start:
    # poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager/wsgi.py
	poetry run manage.py runserver 0.0.0.0:8000

lint:
	poetry run flake8 .