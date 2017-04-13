ExersiseGoogleMaps
==========================

Installation
------------

Create a virtualenv (use ``virtualenvwrapper``): ::

    mkvirtualenv ExersiseGoogleMaps


Install requirements via ``pip``: ::

    pip install django/requirements/development.txt


Create database tables: ::

    # on django/ExersiseGoogleMaps
    ./manage.py syncdb --all --settings=settings.development


Run the project: ::

    # on django/ExersiseGoogleMaps
    ./manage.py runserver --settings=settings.development


Tests
-----

To run the test suite, execute: ::

    make test


To show coverage details (in HTML), use: ::

    make test html