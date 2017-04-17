# -*- coding: utf-8 -*-
from .views import (delete_place, list_place, get_place,
                    parse_model_place, save_response)
from .models import Place
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.test import TestCase


class SimpleTest(TestCase):
    def test_save_place(self):
        id_place = save_response(GOOGLE_RESPONSE)
        place = Place.objects.get(id=id_place)
        self.assertEquals(place.google_place_id, 'ChIJn-sB_xOvogARSbdh0JkB94w')

    def test_delete_place(self):
        place_object = self.save_generic_place()

        self.client.delete(
            reverse(delete_place, args=[place_object.id])
        )

        try:
            Place.objects.get(id=place_object.id)
        except ObjectDoesNotExist:
            pass
        else:
            self.fail('Does not excluded')

    def test_get_place(self):
        place_object = self.save_generic_place()

        self.client.get(
            reverse(get_place, args=[place_object.id])
        )

        try:
            place = Place.objects.get(id=place_object.id)
        except ObjectDoesNotExist:
            self.fail('Does not get place')

        self.assertEquals(place.name, 'name')
        self.assertEquals(place.address, 'address')

    def test_list_places(self):
        self.save_generic_place()

        response = self.client.get(
            reverse(list_place)
        )
        place = response.json().get('result')[0]
        self.assertEquals(place.get('name'), 'name')
        self.assertEquals(place.get('address'), 'address')

    def test_parse_model_place(self):
        place_object = Place(
            name='name',
            address='address',
            latitude='latitude',
            longitude='longitude',
            google_place_id='google_place_id'
        )

        parsed_place = parse_model_place(place_object)
        self.assertEquals(parsed_place.get('name'), 'name')
        self.assertEquals(parsed_place.get('address'), 'address')

    def save_generic_place(self):
        place_object = Place.objects.create(
            name='name',
            address='address',
            latitude='latitude',
            longitude='longitude',
            google_place_id='google_place_id'
        )
        return place_object

GOOGLE_RESPONSE = ('{"result":{"formatted_address":'
                   '"Corcovado - Alto da Boa Vista, Rio de Janeiro - '
                   'State of Rio de Janeiro, Brazil","geometry":'
                   '{"location":{"lat":"-22.95235199999999","lng":'
                   '"-43.2114467"}},"name":"Corcovado","place_id":'
                   '"ChIJn-sB_xOvogARSbdh0JkB94w"}}')
