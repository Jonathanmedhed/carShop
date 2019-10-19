from django.urls import path
from . import views

urlpatterns = [
    path('car', views.car, name='car'),
    path('moto', views.moto, name='moto'),
    path('search', views.search, name='search'),
]