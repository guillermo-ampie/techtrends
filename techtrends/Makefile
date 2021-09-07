# Variables
APP_PORT=3111
CONTAINER_PORT=${APP_PORT}
HOST_PORT=7111
VERSION=1.0.0
DOCKERHUB_ID=gampie
DOCKER_REPOSITORY=techtrends
DOCKER_PATH=${DOCKERHUB_ID}/${DOCKER_REPOSITORY}

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

build-docker:
	docker build  --tag ${DOCKER_PATH}:${VERSION} .

run-docker:
	docker run -d --rm -p ${HOST_PORT}:${CONTAINER_PORT} ${DOCKER_PATH}:${VERSION}
	docker container ls 

push-docker: build-docker
	docker push ${DOCKER_PATH}:${VERSION}


test-endpoints-docker:
	curl localhost:${HOST_PORT}/healthz
	@echo
	curl localhost:${HOST_PORT}/metrics

rm-docker:
	-docker container rm -f  `docker container ls | grep -v CONTAINER | grep ${DOCKER_PATH}:${VERSION} | cut -d" " -f1`
	docker container ls

clean:
	-rm ./database.db

