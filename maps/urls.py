from django.conf.urls import url
from .views import (delete_place, get_place,
                    list_place, search_place, save_place)

urlpatterns = [
    url(r'search/$', search_place),
    url(r'save/$', save_place),
    url(r'list/$', list_place),
    url(r'delete/(?P<id_place>[\d]+)/$', delete_place),
    url(r'get/(?P<id_place>[\d]+)/$', get_place),
]
