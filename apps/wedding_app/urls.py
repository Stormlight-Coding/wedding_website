from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^details', views.details),
    url(r'^accomodations', views.accomodations),
    url(r'^thingstodo', views.thingstodo),
    url(r'^registry', views.registry),
    url(r'^rsvp', views.rsvp),
    url(r'^photos', views.photos),
]
