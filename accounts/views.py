from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from listings.models import Listing
from inquiries.models import Inquiry
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged int')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or Password invalid')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Check if password match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is already in use')
                    return redirect('register')
                else:
                    # All good in the hood
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # Login after register
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        context = {
            'values': request.GET
        }
        return render(request, 'accounts/register.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):
    
    user = request.user

    listings = Listing.objects.order_by('-list_date').filter(user = user)

    inquiries = Inquiry.objects.order_by('-date').exclude(listing = None).filter(user = user)

    # Listing pagination
    paginator = Paginator(listings, 6)  
    page = request.GET.get('page')      
    paged_listings = paginator.get_page(page) 

    # Inquiry pagination
    paginator2 = Paginator(inquiries, 6)  
    page2 = request.GET.get('page2')      
    paged_inquiries = paginator2.get_page(page2) 

    context = {
        'listings': paged_listings,
        'inquiries': paged_inquiries
    }

    return render(request, 'accounts/dashboard.html', context)
