# PiHome client

## To install

Put repository on raspberry pi with connected sensor

Make virtualenv:

`python3 -m venv ~/.envs/pihome`

Activate it:

`source ~/.envs/pihome/bin/activate`

Install requirements:

`pip install -r requirements/base.txt`

Install all required ubuntu libs - for example to use gpio in raspberry pi you have to install:

`sudo apt-get install libgpiod2`

Configure client script:

Put all necessary values into `client/config/base.py`. Sensor UUIDS with wrappers, and server url should be filled out.

## To run

Put command running script `main.py` into some kind of periodic task engine (crontab is more than enough) like this:

`*/5 * * * * /home/pi/.envs/pihome/bin/python3 /home/pi/pihome/client/main.py`

This will call reporting every 5 minutes.