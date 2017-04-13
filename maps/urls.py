from django.conf.urls import url
from .views import search_place

urlpatterns = [
    url(r'search/$', search_place),
]