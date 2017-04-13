# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse, JsonResponse

import json
import urllib


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def search_place(request):
    query_term = request.GET.get('query')
    base_url = settings.GOOGLE_SEARCH_URL
    google_key = settings.GOOGLE_API_KEY

    request_url = '{base_url}?query={query_term}&key={google_key}'.format(
        base_url=base_url,
        query_term=query_term,
        google_key=google_key
    )

    response = urllib.urlopen(request_url)
    return JsonResponse({'response':parse_response(response)})


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
