ExersiseGoogleMaps
==========================

Installation
------------

Create a virtualenv: ::

    virtualenv ExersiseGoogleMaps


Install requirements: ::

    make requirements


Create database tables(MySql): ::
    On MySQL console:
    	create database exersisegooglemaps;

    On project folder:
        make migrate

Run the project: ::

    make run


Tests
-----

To run the test suite, execute: ::

    make test


