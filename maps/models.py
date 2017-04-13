# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    google_place_id = models.CharField(max_length=200)
