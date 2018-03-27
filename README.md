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


# Run mysql in docker container on host

docker pull mysql

docker run -p 3306:3306 --name landing-page-mysql -e MYSQL_ROOT_PASSWORD=toor -d mysql:latest

docker exec -it landing-page-mysql bash

mysql -u root -p

mysql> create database landing_page;

show databases;

docker exec -it landing-page-mysql bash


# Create admin user
python create_user.py


# Get your leads

curl -H "Content-Type: application/json" -X POST -d '{"email":"matt.shirtliffe@aaagag.com","password":"password"}' http://127.0.0.1:5000/auth

curl -H "Content-Type: application/json" -H "Authorization: Bearer token" -X GET  http://127.0.0.1:5000/leads

# Design
## [Start Bootstrap - Landing Page](https://startbootstrap.com/template-overviews/landing-page/)

[Landing Page](http://startbootstrap.com/template-overviews/landing-page/) is a multipurpose landing page template for [Bootstrap](http://getbootstrap.com/) created by [Start Bootstrap](http://startbootstrap.com/).


