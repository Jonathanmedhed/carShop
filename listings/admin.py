from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    #to displayinfo
    list_display = ('id', 'make', 'model', 'is_published', 'price', 'list_date', 'user') 
    #to make them clickable
    list_display_links = ('id', 'make', 'model') 
    #To add filters
    list_filter = ('make', 'model', 'is_published', 'price', 'list_date', 'user') 
    #Make a field editable
    list_editable= ('is_published',)
    #Add search field
    search_fields = ('make', 'model', 'is_published', 'price', 'list_date', 'user', 'city')
    #amount per page
    list_per_page= 25

admin.site.register(Listing, ListingAdmin)
