from django.db import models

class Listing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=255)
    date = models.DateField()
