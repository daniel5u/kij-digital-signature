build:
	sudo pip install --no-input virtualenv
	virtualenv venv || venv/bin/activate && pip install -r requirements.txt

main:
	python3 app/main.py

PHONY: build main