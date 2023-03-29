from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from companies.models import Company
from django.conf import settings

# Create your models here.
class Vehicle(models.Model):
    RegistrationNumber = models.CharField(max_length=255)
    Make = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    EngineNumber = models.CharField(max_length=255)
    ChesisNumber = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vehicle_items')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vehicle_items')
    def __str__(self):
        return self.RegistrationNumber