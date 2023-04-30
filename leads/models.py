from django.db import models
from configurations.models import Cities, Province, Package

# Create your models here.
# i)	Date and time
# Customer Name
# ii)	Customer Contact No.
# iii)	City (select option added in setup)
# iv)	Province
# v)	Package (select from setup)
# vi)	Service Charges (will be taken from package price set in setup but editable)
# vii)	Requirements

class SalesLead(models.Model):
    cutomername = models.CharField(max_length=255)
    ContactNumber = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='customer_city')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='customer_province')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='customer_package')
    requirements  = models.TextField(max_length=255)
    status = models.CharField(max_length=255)
    datetime = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.cutomername
