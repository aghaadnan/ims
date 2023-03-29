from django.db import models
from companies.models import Company
from django.conf import settings

# Create your models here.
class Customer(models.Model):
    Name = models.CharField(max_length=255)
    ContactNumber = models.CharField(max_length=255)
    Address = models.DecimalField(decimal_places=2, max_digits=10)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer_items')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='customer_items')
    def __str__(self):
        return self.name