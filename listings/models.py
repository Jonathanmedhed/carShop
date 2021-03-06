from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Listing(models.Model):
    # Delete listing if user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    millage = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    cc = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)  # can be empty
    # upload to media folder with date
    photo_front = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_back = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_left = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_right = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_extra = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_extra2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    is_in_spotlight = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):  # Main field to display
        return self.model
