.PHONY: migrate
migrate:
	@echo "Migrating database..."
	python3 manage.py migrate --noinput

.PHONY: collectstatic
collectstatic:
	@echo "Copying collectstatic files..."
	python3 manage.py collectstatic --noinput


.PHONY: run
run: migrate collectstatic
	@echo "Running server..."
	python3 manage.py runserver 0.0.0.0:8005