PROJECT_NAME=goro
ENV_DIR=~/python-envs

PROJECT_ENV_DIR=${ENV_DIR}/${PROJECT_NAME}

install: setup

setup:
	test -d PROJECT_ENV_DIR || virtualenv ${PROJECT_ENV_DIR}
	. ${PROJECT_ENV_DIR}/bin/activate; \
		${PROJECT_ENV_DIR}/bin/pip install -r requirements.txt
	touch ${PROJECT_ENV_DIR}/bin/activate

check:
	${PROJECT_ENV_DIR}/bin/activate; pep8 -r ./

deploy: setup
	. ${PROJECT_ENV_DIR}/bin/activate; \
		./manage.py collectstatic --clear --noinput
	. ${PROJECT_ENV_DIR}/bin/activate; \
		./manage.py migrate
	touch ${PROJECT_NAME}/wsgi.py

clean:
	rm -rf static/* ${PROJECT_ENV_DIR}
