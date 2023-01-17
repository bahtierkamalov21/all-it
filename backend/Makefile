.SILENT

install-lib:
	sudo apt install libpq-dev python3-dev

venv: install-lib
	cd backend && rm -rf venv && python3 -m venv venv \
	pip install -r requirements.txt

backend: venv
	cd backend && python3 manage.py makemigrations \
	&& python3 manage.py migrate && python3 manage.py runserver


