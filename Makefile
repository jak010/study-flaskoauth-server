

DOCKER=./docker

run.docker:
	cd $(DOCKER) && sudo docker-compose up -d

flask.run.debug:
	flask run --debug
