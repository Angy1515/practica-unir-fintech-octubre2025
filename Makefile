.PHONY: all $(MAKECMDGOALS)

run:
	docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py palabras.txt yes asc

run-local:
	python3 main.py palabras.txt yes asc

run-local-no-duplicates:
	python3 main.py palabras.txt no asc

run-local-desc:
	python3 main.py palabras.txt yes desc