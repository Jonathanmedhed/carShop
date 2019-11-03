from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import car_make_choices, moto_make_choices, body_types, moto_body_types, colours, cities, price_choices, millage_choices, year_choices, cc_choices


def index(request):
    listings = Listing.objects.filter(is_in_spotlight=True)

    context = {
        'listings': listings,
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
    return render(request, 'pages/index.html', context)

