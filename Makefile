l10n:
	django-admin makemessages -l ru -e html,txt,py
	django-admin compilemessages

setup: l10n
	poetry install
	./manage.py migrate

PORT ?= 8000
start: setup
    poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager/wsgi.py