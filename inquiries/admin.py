from django.contrib import admin
from .models import Inquiry

class InquiryAdmin(admin.ModelAdmin):
    #to displayinfo
    list_display = ('id', 'message', 'user', 'listing' , 'date') 
    #to make them clickable
    list_display_links = ('id', 'message', 'user', 'listing' ) 
    #To add filters
    list_filter = ('id', 'message', 'user', 'listing' , 'date') 
    #Add search field
    search_fields = ('id', 'message', 'user', 'listing' , 'date')
    #amount per page
    list_per_page= 25

admin.site.register(Inquiry, InquiryAdmin)
