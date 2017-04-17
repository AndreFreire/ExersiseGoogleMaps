ExersiseGoogleMaps
==========================

Installation
------------

Create a virtualenv: ::

    virtualenv ExersiseGoogleMaps


Install requirements: ::

    make requirements


Create database tables(MySql): 
    On MySQL console: ::

    	create database exersisegooglemaps;

    On project folder: ::

        make migrate

Run the project: ::

    make run


Tests
-----

To run the test, execute: ::

    make test

Exemples endpoint:
-----

Search Place(GET): ::

    http://localhost:8000/maps/search/?query=corcovado

Save Place(POST): ::

    http://localhost:8000/maps/save/

body:
	google_id_place: ChIJn-sB_xOvogARSbdh0JkB94w

Delete Place(DELETE): ::

	http://localhost:8000/maps/delete/1/

Get saved place(GET): ::
	
	http://localhost:8000/maps/get/1/

List all saved places(GET): ::

	http://localhost:8000/maps/list/


