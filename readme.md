# GeorefXP 2016

## 1.0 Requirements
 
1. Python 2.7 - See [https://www.python.org/]
2. Pip 8.1.X - See [https://pypi.python.org/pypi/pip]
3. Virtual env - See [https://virtualenv.pypa.io/en/stable/]

## 2.0 Guide to install the dependencies


1. To install pip use the following command: $ pip install -U setuptools virtualenv


##3.0 Setting up the developer command

Type:
1. $ virtualenv .
2. $ . bin/activate
3. $ pip install -r requirements.txt

#4.0 To run tests

To execute the battery of tests

- $ ./manage test

To check the tests coverage:

- $ coverage run --source='.' manage.py test [app]

##5.0 For running the application

1. $ cd geoxp/
2. ./manage.py runserver
