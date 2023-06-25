SRC=./src
DOCKER=./docker

venv:
	pip install -r $(SRC)/requirements.txt

flask.db:
	flask db migrate && flask db upgrade

run.docker:
	cd $(DOCKER) && sudo docker-compose up -d

flask.run.debug:
	flask run --debug
