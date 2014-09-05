install: conf

conf:
	pip install -r requirements.txt
	
check:
	pep8 -r ./

deploy:
	./manage.py collectstatic --clear --noinput

clean:
	rm -rf static/*
