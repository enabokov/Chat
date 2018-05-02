run-all:
	docker-compose rm -f -s
	docker-compose up --build --force-recreate -d

lint:
	flake8
	isort --check-only -rc . --diff
