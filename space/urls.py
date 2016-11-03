from django.conf.urls import url
from space.views import planet_list, planet_list_json, planet_create

urlpatterns = [
    url(r'^planet/list/$', planet_list, name='planet_list'),
    url(r'^planet/json/$', planet_list_json, name='planet_list_json'),
    url(r'^planet/create/$', planet_create, name='planet_create')
]
