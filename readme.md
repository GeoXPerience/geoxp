You should have Python 2 installed as well as pip and virtualenv.


If you do not have python installed, run the following command:

$ brew -v update && brew -v install python


If you do not have virtualenv installed, run the following command:

$ pip install -U setuptools virtualenv


To build the development environment:

$ virtualenv .
$ . bin/activate
$ pip install -r requirements.txt


You should also run the tests:

$ ./mange test


To check the tests coverage:

$ coverage run --source='.' manage.py test [app]


To run the application use the following commands:

$ cd geoxp/
$ ./manage.py runserver
