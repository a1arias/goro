PROJECT_NAME=goro
ENV_DIR=~/python-envs

PROJECT_ENV_DIR=${ENV_DIR}/${PROJECT_NAME}

install: setup

setup:
	virtualenv ${PROJECT_ENV_DIR}
	${PROJECT_ENV_DIR}/bin/pip install -r requirements.txt

check:
	${PROJECT_ENV_DIR}/bin/pep8 -r ./

deploy: setup
	./manage.py collectstatic --clear --noinput
	touch goro/wsgi.py

clean:
	rm -rf static/* ${PROJECT_ENV_DIR}
