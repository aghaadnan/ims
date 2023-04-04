from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from companies.models import Company
from customers.models import Customer
from inventory.models import TrackerDevice, Sim
from django.conf import settings

# Create your models here.
class Vehicle(models.Model):
    RegistrationNumber = models.CharField(max_length=255)
    Make = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    EngineNumber = models.CharField(max_length=255)
    ChesisNumber = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='vehicle_items', null=True)
    trackerDevice = models.ForeignKey(TrackerDevice, on_delete=models.CASCADE, related_name='vehicle_items', null=True)
    sim = models.ForeignKey(Sim, on_delete=models.CASCADE, related_name='vehicle_items', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vehicle_items')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vehicle_items')
    isTrackerInstalled = models.BooleanField(default=False)
    def __str__(self):
        return self.RegistrationNumber