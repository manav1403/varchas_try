from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("vol",views.login),
    path("vol/logedin",views.vol_logedin),
    path("vol/game",views.game),
    path("vol/update",views.update),
    path("",views.live),
]