from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from configurations.models import Countries, Cities, Subscriptions

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
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='owned_cities')
    contactperson = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email   = models.EmailField(blank=True)
    GST = models.CharField(max_length=255)
    NTN = models.CharField(max_length=255)
    package = models.ForeignKey(Subscriptions, on_delete=models.CASCADE, related_name='owned_subscription')
    is_active = models.BooleanField(default=True)
    is_expired = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    renew_date = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_companies')

    def __str__(self):
        return self.name


class EmailTemplate(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='email_templates')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    email_date = models.DateField()
    days_before_expiry = models.PositiveIntegerField()

    def __str__(self):
        return self.subject