from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing
from .choices import car_make_choices, moto_make_choices, body_types, moto_body_types, colours, cities, price_choices, millage_choices, year_choices, cc_choices
from django.core.files.storage import FileSystemStorage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages


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


def listing_form(request):
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
        photo_extra = request.FILES.get('photo_extra')
        if photo_extra is not None:
            photo_extra_name = fs.save(photo_extra.name, photo_extra)
        photo_extra2 = request.FILES.get('photo_extra2')
        if photo_extra2 is not None:
            photo_extra2_name = fs.save(photo_extra2.name, photo_extra2)

        listing = Listing(user_id=user_id, make=make, model=model, cc=cc, year=year, body=body, colour=colour, price=price,
                          millage=millage, city=city, description=description, photo_front=photo_front_name, photo_back=photo_back_name,
                          photo_left=photo_left_name, photo_right=photo_right_name, photo_extra=photo_extra_name, photo_extra2=photo_extra2_name)
        listing.save()
        messages.success(request, 'Listing Published!')
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
    return render(request, 'listings/listing_form.html', context)


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
    if 'minprice' or 'maxprice' in request.GET:
        minprice = request.GET.get('minprice')
        maxprice = request.GET.get('maxprice')
        if minprice is not None:
            queryset_list = queryset_list.filter(price__gte=minprice)
        if maxprice is not None:
            queryset_list = queryset_list.filter(price__lte=maxprice)

    # millage
    if 'minmillage' or 'maxmillage' in request.GET:
        minmillage = request.GET.get('minmillage')
        maxmillage = request.GET.get('maxmillage')
        if minmillage is not None:
            queryset_list = queryset_list.filter(millage__gte=minmillage)
        if maxmillage is not None:
            queryset_list = queryset_list.filter(millage__lte=maxmillage)

    # year
    if 'minyear' or 'maxyear' in request.GET:
        minyear = request.GET.get('minyear')
        maxyear = request.GET.get('maxyear')
        if minyear is not None:
            queryset_list = queryset_list.filter(year__gte=minyear)
        if maxyear is not None:
            queryset_list = queryset_list.filter(year__lte=maxyear)

    # cc
    if 'mincc' or 'maxcc' in request.GET:
        mincc = request.GET.get('mincc')
        maxcc = request.GET.get('maxcc')
        if mincc is not None:
            queryset_list = queryset_list.filter(cc__gte=mincc)
        if maxcc is not None:
            queryset_list = queryset_list.filter(cc__lte=maxcc)

    # type
    if 'type' in request.GET:
        type = request.GET['type']
        if type == 'moto':
            queryset_list = queryset_list.exclude(cc=None)
        elif type == 'car':
            queryset_list = queryset_list.filter(cc=None)

    # pagination
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

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
        'listings': paged_listings,
        'values': request.GET  # to mantain search values in the fields after search
    }

    return render(request, 'listings/search.html', context)
