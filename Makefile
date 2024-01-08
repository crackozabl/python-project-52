init:
	poetry install

l10n:
	poetry run python ./manage.py makemessages -l ru -e html,txt,py
	poetry run python ./manage.py compilemessages

db:
	poetry run python ./manage.py migrate

setup: init l10n db

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi
	#poetry run python ./manage.py runserver 0.0.0.0:$(PORT)

lint:
	poetry run flake8 .

test:
	coverage run --source="./task_manager" manage.py test
	coverage html

