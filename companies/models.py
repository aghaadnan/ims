from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Company(models.Model):
    PACKAGES = [
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]
    CITIES = [
        ('LAHORE', 'LAHORE'),
        ('ISLAMABAD', 'ISLAMABAD'),
    ]
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, choices=CITIES  )
    contactperson = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email   = models.EmailField(blank=True)
    GST = models.CharField(max_length=255)
    NTN = models.CharField(max_length=255)
    package = models.CharField(max_length=255, choices=PACKAGES)
    is_active = models.BooleanField(default=True)
    is_expired = models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_companies')

    def __str__(self):
        return self.name
