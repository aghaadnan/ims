from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from companies.models import Company
from django.conf import settings


    
class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='users')
    groups = models.ManyToManyField(Group, blank=True, related_name='users_inventory')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='users_inventory')



class Inventory(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inventory_items')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='inventory_items')

    def __str__(self):
        return self.name

class TrackerDevice(models.Model):
    model_number = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    imei = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trackerdevice_items')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='trackerdevice_items')
    def __str__(self):
        return self.model_number
    

class Sim(models.Model):
    MSISDN = models.CharField(max_length=50)
    ICC_ID = models.CharField(max_length=50)
    OPERATOR_CHOICES = [
        ('zong', 'Zong'),
        ('ufone', 'Ufone'),
        ('warid', 'Warid'),
        ('mobilink', 'Mobilink'),
        ('telenor', 'Telenor'),
    ]

    GSM_CHOICES = [
        ('2g', '2G'),
        ('3g', '3G'),
    ]
    OPERATOR = models.CharField(max_length=50, choices=OPERATOR_CHOICES)
    SIM_TYPE = models.CharField(max_length=50, choices=GSM_CHOICES)
    PACKAGE = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sim_items')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sim_items')
    def __str__(self):
        return self.MSISDN
    


