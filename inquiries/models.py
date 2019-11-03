from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from listings.models import Listing


class Inquiry(models.Model):
    # Delete listing if user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField(blank=True)  # can be empty
    # upload to media folder with date
    file = models.FileField(upload_to='files/%Y/%m/%d/', blank=True)
    file2 = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):  # Main field to display
        return self.message

