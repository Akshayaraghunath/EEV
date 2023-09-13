from django.db import models
from django.contrib.auth.models import User


class charge(models.Model):
    station_name=models.CharField(max_length=100,null=True)
    vehicle_category=models.IntegerField(default=True)
    Location=models.CharField(max_length=100,null=True)
    Price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='vehicle_images',null=True)

class Service(models.Model):
    station_name=models.CharField(max_length=100)
    vehicle_category=models.IntegerField(default=True)
    Type_of_service=models.CharField(max_length=100,null=True)
    Location=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to='vehicle_images',null=True)



    

    

# Create your models here.
