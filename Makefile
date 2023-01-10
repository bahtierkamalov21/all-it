.SILENT:

venv:
	cd backend && rm -r venv && python -m venv venv

venv_windows:
	cd backend && rd /s /q venv && python -m venv venv

migrate:
	python manage.py makemigrations && python manage.py migrate

backend: venv migrate
	python manage.py runserver

backend_windows: venv_windows migrate
	python manage.py runserver

frontend:
	cd ../ && npm install && npm run lint --fix

developed: backend frontend
	npm run serve

developed_windows: backend_windows frontend
	npm run serve

production: backend frontend
	npm run build

production_windows: backend_windows frontend
	npm run build
