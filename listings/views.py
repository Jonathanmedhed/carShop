from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing
from .choices import car_make_choices, moto_make_choices, body_types, moto_body_types, colours, cities, price_choices, millage_choices, year_choices, cc_choices
from django.core.files.storage import FileSystemStorage


def carousel(request):
    listings = Listing.objects.filter(is_in_spotlight=True)

    context = {
        'listings': listings,
    }
    return render(request, 'templates/partials/_carousel.html', context)

def listing(request, listing_id):
    
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def car(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        # Get form values
        user_id = request.POST['user_id']
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        body = request.POST['body']
        colour = request.POST['colour']
        price = request.POST['price']
        millage = request.POST['millage']
        city = request.POST['city']
        description = request.POST['description']
        photo_front = request.FILES['photo_front']
        photo_front_name = fs.save(photo_front.name, photo_front)
        photo_back = request.FILES['photo_back']
        photo_back_name = fs.save(photo_back.name, photo_back)
        photo_left = request.FILES['photo_left']
        photo_left_name = fs.save(photo_left.name, photo_left)
        photo_right = request.FILES['photo_right']
        photo_right_name = fs.save(photo_right.name, photo_right)
        photo_extra = request.FILES['photo_extra']
        photo_extra_name = fs.save(photo_extra.name, photo_extra)
        photo_extra2 = request.FILES['photo_extra2']
        photo_extra2_name = fs.save(photo_extra2.name, photo_extra2)

        listing = Listing(user_id=user_id, make=make, model=model, year=year, body=body, colour=colour, price=price,
                          millage=millage, city=city, description=description, photo_front=photo_front_name, photo_back=photo_back_name,
                          photo_left=photo_left_name, photo_right=photo_right_name, photo_extra=photo_extra_name, photo_extra2=photo_extra2_name)
        listing.save()
        return redirect('dashboard')
    else:
        listings = Listing.objects.all()
    context = {
        'car_make_choices': car_make_choices,
        'moto_make_choices': moto_make_choices,
        'body_types': body_types,
        'moto_body_types': moto_body_types,
        'colours': colours,
        'cities': cities,
        'price_choices': price_choices,
        'millage_choices': millage_choices,
        'year_choices': year_choices,
        'values': request.GET
    }
    return render(request, 'listings/car.html', context)


def moto(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        # Get form values
        user_id = request.POST['user_id']
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        cc = request.POST['cc']
        body = request.POST['body']
        colour = request.POST['colour']
        price = request.POST['price']
        millage = request.POST['millage']
        city = request.POST['city']
        description = request.POST['description']
        photo_front = request.FILES['photo_front']
        photo_front_name = fs.save(photo_front.name, photo_front)
        photo_back = request.FILES['photo_back']
        photo_back_name = fs.save(photo_back.name, photo_back)
        photo_left = request.FILES['photo_left']
        photo_left_name = fs.save(photo_left.name, photo_left)
        photo_right = request.FILES['photo_right']
        photo_right_name = fs.save(photo_right.name, photo_right)
        photo_extra = request.FILES['photo_extra']
        photo_extra_name = fs.save(photo_extra.name, photo_extra)
        photo_extra2 = request.FILES['photo_extra2']
        photo_extra2_name = fs.save(photo_extra2.name, photo_extra2)

        listing = Listing(user_id=user_id, make=make, model=model, cc=cc,year=year, body=body, colour=colour, price=price,
                          millage=millage, city=city, description=description, photo_front=photo_front_name, photo_back=photo_back_name,
                          photo_left=photo_left_name, photo_right=photo_right_name, photo_extra=photo_extra_name, photo_extra2=photo_extra2_name)
        listing.save()
        return redirect('dashboard')
    else:
        listings = Listing.objects.all()
    context = {
        'car_make_choices': car_make_choices,
        'moto_make_choices': moto_make_choices,
        'body_types': body_types,
        'moto_body_types': moto_body_types,
        'colours': colours,
        'cc_choices': cc_choices,
        'cities': cities,
        'price_choices': price_choices,
        'millage_choices': millage_choices,
        'year_choices': year_choices,
        'values': request.GET
    }
    return render(request, 'listings/moto.html', context)


def search(request):

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

    # cc
    if 'mincc' and 'maxcc' in request.GET:
        mincc = request.GET['mincc']
        maxcc = request.GET['maxcc']
        if mincc and maxcc:
            queryset_list = queryset_list.filter(
                cc__gte=mincc, cc__lte=maxcc)
    elif 'mincc' in request.GET:
        mincc = request.GET['mincc']
        if mincc:
            queryset_list = queryset_list.filter(
                cc__gte=mincc)
    elif 'maxcc' in request.GET:
        maxcc = request.GET['maxcc']
        if maxcc:
            queryset_list = queryset_list.filter(
                cc__lte=maxcc)
    # type
    if 'type' in request.GET:
        type = request.GET['type']
        if type == 'moto':
            queryset_list = queryset_list.exclude(cc=None)
        elif type == 'car':
            queryset_list = queryset_list.filter(cc=None)

    context = {
        'car_make_choices': car_make_choices,
        'moto_make_choices': moto_make_choices,
        'body_types': body_types,
        'moto_body_types': moto_body_types,
        'body_types': body_types,
        'colours': colours,
        'cities': cities,
        'price_choices': price_choices,
        'millage_choices': millage_choices,
        'year_choices': year_choices,
        'cc_choices': cc_choices,
        'listings': queryset_list,
        'values': request.GET  # to mantain search values in the fields after search
    }

    return render(request, 'listings/search.html', context)


def search_car(request):

    queryset_list = Listing.objects.order_by('-list_date').filter(cc=None)

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
        'moto_body_types': moto_body_types,
        'colours': colours,
        'cities': cities,
        'price_choices': price_choices,
        'millage_choices': millage_choices,
        'year_choices': year_choices,
        'listings': queryset_list,
        'values': request.GET  # to mantain search values in the fields after search
    }

    return render(request, 'listings/search_car.html', context)
