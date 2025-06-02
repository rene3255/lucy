.PHONY: delete-all-migrations run mkmig mig load-metaltypes load-countries
APPS_NAME := $(shell find . -maxdepth 3 -type d -name migrations -exec dirname {} \; | sed 's|^\./||' | sort | uniq)

delete-all-migrations:
	@for app in $(APPS_NAME); do \
		if [ -d "$$app/migrations" ]; then \
			echo "cleanging migrations $$app..."; \
			find "$$app/migrations" -name "*.py" ! -name "__init__.py" -delete; \
			find "$$app/migrations" -name "*.pyc" -delete; \
			app_name = $$(basename "$$app"); \
			echo "Borrando las migraciones para la aplicación $$app_name de la base de datos"; \
			echo "DELETE FROM django_migrations WHERE app = '$$app_name';" | python manage.py dbshell; \
			echo "Se concluyo la app $$app"; \
		fi; \
	done
run:
	python manage.py runserver 0.0.0.0:8000
mkmig:
	pip install --upgrade pip && \
	python manage.py makemigrations 

mig:
	python manage.py migrate
load-metaltypes:
	python manage.py loaddata applications/reference_data/fixtures/metal_type.json
load-countries:
	python manage.py loaddata applications/reference_data/fixtures/country.json
