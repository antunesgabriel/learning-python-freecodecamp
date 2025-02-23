setup:
	python3 -m venv .venv

generate-requirements:
	pip freeze > requirements.txt

install-requirements:
	pip install -r requirements.txt

run:
	python3 main.py
