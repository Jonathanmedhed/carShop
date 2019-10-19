from django.shortcuts import render
from django.http import HttpResponse

def car(request):
    return render(request, 'listings/car.html')

def moto(request):
    return render(request, 'listings/moto.html')

def search(request):
    return render(request, 'listings/search.html')