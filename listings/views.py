from django.shortcuts import render
from .models import Listing
from .choices import car_make_choices, moto_make_choices


def car(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/car.html', context)


def moto(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/moto.html', context)

'''
def search_car(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Make
    if 'make' in request.GET:
        make = request.GET['make']
        if make:
            queryset_list = queryset_list.filter(
                make__iexact=make)

    # Model
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            queryset_list = queryset_list.filter(
                model__iexact=model)

    #Body
    if 'body' in request.GET:
        body = request.GET['body']
        if body:
            queryset_list = queryset_list.filter(
                body__iexact=body)

    #Colour
    if 'colour' in request.GET:
        colour = request.GET['colour']
        if colour:
            queryset_list = queryset_list.filter(
                colour__iexact=colour)

    context = {
        'car_make_choices': car_make_choices,
        'moto_make_choices': moto_make_choices,
        'listings': queryset_list,
        'values': request.GET #to mantain search values in the fields after search
    }
    return render(request, 'listings/search_car.html', context)

'''
def search_moto(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/search_moto.html', context)

def search_car(request):
    
    queryset_list = Listing.objects.order_by('-list_date')
    
    # State
    if 'make' in request.GET:
        make = request.GET['make']
        if make:
            queryset_list = queryset_list.filter(
                make__iexact=make)

    context = {
        'car_make_choices': car_make_choices,
        'moto_make_choices': moto_make_choices,
        'listings': queryset_list,
        'values': request.GET #to mantain search values in the fields after search
    }

    return render(request, 'listings/search_car.html', context)