run-chat-server:
	python runner.py

lint:
	flake8
	isort --check-only -rc . --diff

