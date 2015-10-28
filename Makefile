#
# Environment
#

create_virtual_environment:
	virtualenv metube_environment

enter-virtual-environment:
	source metube_environment/bin/activate

install-dependencies:
	pip install --upgrade -r requirements.txt

#
# Docker
#

build-metube-web:
	docker build -t "metube/web" .

compose-up:
	docker-compose -p metube up -d

#
# Testing
#

code-pylint:
	pylint --load-plugins pylint_django backend/

code-coverage:
	python manage.py test