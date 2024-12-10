from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.username

class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        return self.model