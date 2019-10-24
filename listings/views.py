from django.shortcuts import render
from .models import Listing
from .choices import car_make_choices, moto_make_choices, body_types, colours, cities, price_choices, millage_choices, year_choices


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


def search_moto(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/search_moto.html', context)


def search_car(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # make
    if 'make' in request.GET:
        make = request.GET['make']
        if make:
            queryset_list = queryset_list.filter(
                make__iexact=make)

    # model
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            queryset_list = queryset_list.filter(
                model__iexact=model)

    # Body
    if 'body' in request.GET:
        body = request.GET['body']
        if body:
            queryset_list = queryset_list.filter(
                body__iexact=body)

    # Colour
    if 'colour' in request.GET:
        colour = request.GET['colour']
        if colour:
            queryset_list = queryset_list.filter(
                colour__iexact=colour)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # price
    if 'minprice' and 'maxprice' in request.GET:
        minprice = request.GET['minprice']
        maxprice = request.GET['maxprice']
        if minprice and maxprice:
            queryset_list = queryset_list.filter(
                price__gte=minprice, price__lte=maxprice)
    elif 'minprice' in request.GET:
        minprice = request.GET['minprice']
        if minprice:
            queryset_list = queryset_list.filter(
                price__gte=minprice)
    elif 'maxprice' in request.GET:
        maxprice = request.GET['maxprice']
        if maxprice:
            queryset_list = queryset_list.filter(
                price__lte=maxprice)

    # millage
    if 'minmillage' and 'maxmillage' in request.GET:
        minmillage = request.GET['minmillage']
        maxmillage = request.GET['maxmillage']
        if minmillage and maxmillage:
            queryset_list = queryset_list.filter(
                millage__gte=minmillage, millage__lte=maxmillage)
    elif 'minmillage' in request.GET:
        minmillage = request.GET['minmillage']
        if minmillage:
            queryset_list = queryset_list.filter(
                millage__gte=minmillage)
    elif 'maxmillage' in request.GET:
        maxmillage = request.GET['maxmillage']
        if maxmillage:
            queryset_list = queryset_list.filter(
                millage__lte=maxmillage)

    # year
    if 'minyear' and 'maxyear' in request.GET:
        minyear = request.GET['minyear']
        maxyear = request.GET['maxyear']
        if minyear and maxyear:
            queryset_list = queryset_list.filter(
                year__gte=minyear, year__lte=maxyear)
    elif 'minyear' in request.GET:
        minyear = request.GET['minyear']
        if minyear:
            queryset_list = queryset_list.filter(
                year__gte=minyear)
    elif 'maxyear' in request.GET:
        maxyear = request.GET['maxyear']
        if maxyear:
            queryset_list = queryset_list.filter(
                year__lte=maxyear)

    context = {
        'car_make_choices': car_make_choices,
        'moto_make_choices': moto_make_choices,
        'body_types': body_types,
        'colours': colours,
        'cities': cities,
        'price_choices': price_choices,
        'millage_choices': millage_choices,
        'year_choices': year_choices,
        'listings': queryset_list,
        'values': request.GET  # to mantain search values in the fields after search
    }

    return render(request, 'listings/search_car.html', context)
