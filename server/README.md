# PiHome server

## To install

Make virtualenv:

`pyhon3 -m venv ~/.envs/pihome`

Activate it:

`source ~/.envs/pihome/bin/activate`

Install requirements:

`pip install -r requirements/base.txt`

Make migrations:

`python manage.py migrate`

Run devserver:

`python manage.py runserver`

Or run production server using all necessary precautions (collectstatic, static sering, modify settings for your database of choice, etc.)

## Usage

* Add sensor in django admin - note its UUID
* Note server url
* Configure client software using noted data.