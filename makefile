install:
	pip3 install virtualenv
	virtualenv venv
	source venv/bin/activate
	venv\Scripts\activate
	pip3 install -r requirements.txt
	python3 manage.py test
	python3 manage.py runserver
