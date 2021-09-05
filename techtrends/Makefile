# Variables
APP_PORT=3111

setup:
	pip3 install --upgrade --user pip
	pip3 install --upgrade --user pipenv
	pipenv --python 3.8
	# Use the virtual env with:
	pipenv shell

install:
	@echo; echo ">>> This should be run inside a virtual env: pipenv shell"
	@echo; echo "Let pipenv create the 'Pipfile' from the 'requirements.txt' file"; echo
	pipenv install yapf
	yapf --version
	pipenv install -r requirements.txt

init:
	@./build_db.sh

run: init
	python ./app.py

test-endpoints:
	curl localhost:${APP_PORT}/healthz
	@echo
	curl localhost:${APP_PORT}/metrics

