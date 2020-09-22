# PiHome client

## To install

Put repository on raspberry pi with connected sensor

Make virtualenv:

`python3 -m venv ~/.envs/pihome`

Activate it:

`source ~/.envs/pihome/bin/activate`

Install requirements:

`pip install -r requirements/base.txt`

Configure client script:

* put sensor UUID into SENSOR_UUID setting in `client/config/base.py`
* put server url into SERVER_ENDPOINT setting in `client/config/base.py`
* set valid LIBRARY_WRAPPER in `client/config/base.py`

