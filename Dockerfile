# docker build -f Dockerfile -t matthewshirtliffecouk/landing_page .
# docker run -d --name landing-page-mysql mysql
# docker run -d -p 5000:5000 --link landing-page-mysql:mysql --name landing-page  matthewshirtliffecouk/landing_page

FROM python:3.6

MAINTAINER Matthew Shirtliffe

ENV SECRET="kjbkjbkgunmn vjhv"
ENV APP_SETTINGS="development"
ENV DATABASE_URL="mysql+pymysql://root:toor@landing-page-mysql/landing_page"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
