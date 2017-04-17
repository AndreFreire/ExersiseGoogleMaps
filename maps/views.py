# -*- coding: utf-8 -*-
from .models import Place
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import json
import urllib


@csrf_exempt
@require_http_methods(["GET"])
def search_place(request):
    query_term = request.GET.get('query')
    base_url = settings.GOOGLE_SEARCH_URL
    google_key = settings.GOOGLE_API_KEY

    request_url = '{base_url}?query={query_term}&key={google_key}'.format(
        base_url=base_url,
        query_term=query_term,
        google_key=google_key
    )
    try:
        http_response = urllib.urlopen(request_url)
    except IOError:
        return JsonResponse(
            {'message': 'Connection failure'},
            status=503
        )

    response = parse_response(http_response)

    return JsonResponse({'response': response})


@csrf_exempt
@require_http_methods(["POST"])
def save_place(request):
    google_id_place = request.POST.get('google_id_place')
    base_url = settings.GOOGLE_DETAIL_URL
    google_key = settings.GOOGLE_API_KEY

    request_url = '{base_url}?placeid={google_id_place}&key={google_key}'.format(
        base_url=base_url,
        google_id_place=google_id_place,
        google_key=google_key
    )
    try:
        response = urllib.urlopen(request_url)
    except IOError:
        return JsonResponse(
            {'message': 'Connection failure'},
            status=503
        )

    saved_id = save_response(response.read())

    return JsonResponse({
        'message': 'Success',
        'id': saved_id
    })


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_place(request, id_place):
    try:
        Place.objects.get(id=id_place).delete()
    except ObjectDoesNotExist:
        return JsonResponse(
            {'message': 'Not Found'},
            status=404
        )

    return JsonResponse({
        'message': 'Success'
    })


@csrf_exempt
@require_http_methods(["GET"])
def list_place(request):
    places = Place.objects.all()
    json_places = []

    for place in places:
        json_places.append(parse_model_place(place))

    if json_places:
        return JsonResponse({'result': json_places})

    return JsonResponse(
        {'message': 'Not Found'},
        status=404
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_place(request, id_place):
    try:
        place = Place.objects.get(id=id_place)
    except ObjectDoesNotExist:
        return JsonResponse(
            {'message': 'Not Found'},
            status=404
        )

    return JsonResponse({
        'message': 'Success',
        'result': parse_model_place(place)
    })


def save_response(response):
    jsonData = json.loads(response)
    result = jsonData.get('result', {})
    place_object = Place.objects.create(
        name=result.get('name'),
        address=result.get('formatted_address'),
        latitude=result.get('geometry').get('location').get('lat'),
        longitude=result.get('geometry').get('location').get('lng'),
        google_place_id=result.get('place_id')
    )
    return place_object.id


def parse_response(response):
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)
    results = jsonData.get('results', {})
    parsed_result = []
    for item in results:
        parsed_result.append({
            'name': item.get('name'),
            'address': item.get('formatted_address'),
            'latitude': item.get('geometry').get('location').get('lat'),
            'longitude': item.get('geometry').get('location').get('lng'),
            'google_place_id': item.get('place_id')
        })
    return parsed_result


def parse_model_place(obj):
    parsed_object = {
        'id': obj.id,
        'name': obj.name,
        'address': obj.address,
        'latitude': obj.latitude,
        'longitude': obj.longitude,
        'google_place_id': obj.google_place_id
    }
    return parsed_object
