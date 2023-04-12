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
class TrackerDeviceVendor(models.Model):
    vendor = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.vendor

class TrackerDeviceModel(models.Model):
    model_number = models.CharField(max_length=255)
    vendor = models.ForeignKey(TrackerDeviceVendor, on_delete=models.CASCADE, related_name='trackerdevice_vendor')
    def __str__(self):
        return self.model_number

class TrackerDevice(models.Model):
    
    # MODEL_CHOICES = [
    #     ('fmB920', 'FMB920'),
    #     ('FMB125', 'FMB125'),
    #     ('fmt100', 'FMT100'),
    #     ('gv300', 'GV300'),
    #     ('gv55', 'GV55'),
    # ]

    # VENDOR_CHOICES = [
    #     ('teltonika', 'Teltonika'),
    #     ('queclink', 'Queclink'),
    # ]
    # model_number = models.CharField(max_length=255, choices=MODEL_CHOICES)
    # vendor = models.CharField(max_length=255, choices=VENDOR_CHOICES)
    model_number = models.ForeignKey(TrackerDeviceModel, on_delete=models.CASCADE, related_name='trackerdevice_items')
    imei = models.CharField(max_length=255)
    isUsed = models.BooleanField(default=False)
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
    isUsed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sim_items')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sim_items')
    def __str__(self):
        return self.MSISDN
    


