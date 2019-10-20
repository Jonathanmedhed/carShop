from django.shortcuts import render
from django.http import HttpResponse

def car(request):
    return render(request, 'listings/car.html')

def moto(request):
    return render(request, 'listings/moto.html')

def search_car(request):
    return render(request, 'listings/search_car.html')

def search_moto(request):
    return render(request, 'listings/search_moto.html')