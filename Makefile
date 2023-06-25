SRC=./src
DOCKER=./docker

export PYTHONPATH=$(PWD):$PYTHONPATH

venv:
	pip install -r $(SRC)/requirements.txt

db.patch: db.migrate db.upgrade

db.init:
	flask db init

db.migrate:
	flask db migrate

db.upgrade:
	flask db upgrade

run.docker:
	cd $(DOCKER) && sudo docker-compose up -d

flask.run.debug:
	flask run --debug
