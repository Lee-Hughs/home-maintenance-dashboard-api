start:
	docker-compose up

test:
	python -m coverage run -m pytest tests
