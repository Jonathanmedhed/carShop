from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Inquiry, Listing
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from listings.choices import car_make_choices, moto_make_choices, body_types, moto_body_types, colours, cities, price_choices, millage_choices, year_choices, cc_choices


def inquiry(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # Check if user has made a inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Inquiry.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an enquiry for this vehicle')
                return redirect('/listings/'+listing_id)

        inquiry = Inquiry(listing_id=listing_id,
                          message=message, user_id=user_id)
        inquiry.save()

        # Send Mail
        '''
        send_mail(
            #Title
            'Property Listing Inquiry', 
            #Body
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            #Source
            'jonathanmedhed@gmail.com',
            #Dest
            [listing.user.email,'jonathanmedhed@gmail.com'],
            fail_silently=False
        )
        '''

        messages.success(request, 'Your request has been submited')

        return redirect('/listings/'+listing_id)


def cvinquiry(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        message = request.POST['message']
        user_id = request.POST['user_id']
        file = request.FILES.get('file')
        file_name = fs.save(file.name, file)
        file2 = request.FILES.get('file2')
        if file2 is not None:
            file2_name = fs.save(file2.name, file2)
            inquiry = Inquiry(message=message, user_id=user_id,
                              file=file_name, file2=file2_name)
            inquiry.save()
        else:
            inquiry = Inquiry(message=message, user_id=user_id,
                              file=file_name)
            inquiry.save()

        # Send Mail
        '''
        send_mail(
            #Title
            'Property Listing Inquiry', 
            #Body
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            #Source
            'jonathanmedhed@gmail.com',
            #Dest
            [listing.user.email,'jonathanmedhed@gmail.com'],
            fail_silently=False
        )
        '''

        messages.success(request, 'Your request has been submited')

        return redirect('/')


def dealerinquiry(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        message = request.POST['message']
        user_id = request.POST['user_id']
        # Make post optional
        file = request.FILES.get('file')
        if file is not None:
            file_name = fs.save(file.name, file)
            inquiry = Inquiry(message=message, user_id=user_id,
                              file=file_name)
            inquiry.save()
        else:
            inquiry = Inquiry(message=message, user_id=user_id)

            inquiry.save()

        # Send Mail
        '''
        send_mail(
            #Title
            'Property Listing Inquiry', 
            #Body
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            #Source
            'jonathanmedhed@gmail.com',
            #Dest
            [listing.user.email,'jonathanmedhed@gmail.com'],
            fail_silently=False
        )
        '''

        messages.success(request, 'Your request has been submited')

        return redirect('/')


def appraisalinquiry(request):
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
        photo_extra2 = request.FILES.get('photo_extra2')
        if photo_extra is not None and photo_extra2 is not None:
            photo_extra_name = fs.save(photo_extra.name, photo_extra)
            photo_extra2_name = fs.save(photo_extra2.name, photo_extra2)
            listing = Listing(user_id=user_id, make=make, model=model, cc=cc, year=year, body=body, colour=colour, price=price,
                              millage=millage, city=city, description=description, photo_front=photo_front_name, photo_back=photo_back_name,
                              photo_left=photo_left_name, photo_right=photo_right_name, photo_extra=photo_extra_name, photo_extra2=photo_extra2_name, is_published=False)
            listing.save()
            return redirect('/')
        elif photo_extra is not None and photo_extra2 is None:
            photo_extra_name = fs.save(photo_extra.name, photo_extra)
            listing = Listing(user_id=user_id, make=make, model=model, cc=cc, year=year, body=body, colour=colour, price=price,
                              millage=millage, city=city, description=description, photo_front=photo_front_name, photo_back=photo_back_name,
                              photo_left=photo_left_name, photo_right=photo_right_name, photo_extra=photo_extra_name, is_published=False)
            listing.save()
            return redirect('/')
        elif photo_extra2 is not None and photo_extra is None:
            photo_extra_name = fs.save(photo_extra.name, photo_extra)
            listing = Listing(user_id=user_id, make=make, model=model, cc=cc, year=year, body=body, colour=colour, price=price,
                              millage=millage, city=city, description=description, photo_front=photo_front_name, photo_back=photo_back_name,
                              photo_left=photo_left_name, photo_right=photo_right_name, photo_extra2=photo_extra2_name, is_published=False)
            listing.save()
            return redirect('/')

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

    messages.success(request, 'Your request has been submited')

    return render(request, 'listings/listing_form.html', context)
