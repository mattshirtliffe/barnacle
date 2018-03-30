# Running
pipenv --python 3.6

pipenv shell

pipenv install

export FLASK_APP="run.py"

export SECRET="your choice"

export APP_SETTINGS="development"

export DATABASE_URL="mysql+pymysql://root:toor@localhost/landing_page"


# Database and Migrations

python manage.py db init

python manage.py db migrate

python manage.py db upgrade


# Database and Migrations Docker

docker exec -it landing-page python manage.py db upgrade




# Run tests

python manage.py test

# Run mysql in docker container on host

docker pull mysql

docker run -p 3306:3306 --name landing-page-mysql -e MYSQL_ROOT_PASSWORD=toor -d mysql:latest

docker exec -it landing-page-mysql bash

mysql -u root -p

create database landing_page;

show databases;

docker exec -it landing-page-mysql bash


# Create admin user
python create_user.py


# Get your leads

curl -H "Content-Type: application/json" -X POST -d '{"email":"email","password":"password"}' http://127.0.0.1:5000/auth

curl -H "Content-Type: application/json" -H "Authorization: Bearer token" -X GET  http://127.0.0.1:5000/leads

# Design
## [Start Bootstrap - Landing Page](https://startbootstrap.com/template-overviews/landing-page/)

[Landing Page](http://startbootstrap.com/template-overviews/landing-page/) is a multipurpose landing page template for [Bootstrap](http://getbootstrap.com/) created by [Start Bootstrap](http://startbootstrap.com/).


# Docker Build

docker build -f Dockerfile -t matthewshirtliffecouk/landing_page .

docker run -d --name landing-page-mysql mysql

docker run -d -p 5000:5000 --link landing-page-mysql:mysql --name landing-page  matthewshirtliffecouk/landing_page

docker exec -it landing-page-mysql bash

mysql -u root -p

create database landing_page;