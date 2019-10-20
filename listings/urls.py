from django.urls import path
from . import views

urlpatterns = [
    path('car', views.car, name='car'),
    path('moto', views.moto, name='moto'),
    path('search_car', views.search_car, name='search_car'),
    path('search_moto', views.search_moto, name='search_moto'),
]