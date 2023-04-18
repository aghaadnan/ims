from django.db import models

# Create your models here.
class Countries(models.Model):
    country = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    
    def __str__(self):
        return self.country

class Cities(models.Model):
    city = models.CharField(max_length=255)
    
    def __str__(self):
        return self.city
class Subscriptions(models.Model):
    subscription = models.CharField(max_length=255)
    days = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    datetime = models.DateTimeField()

    
    def __str__(self):
        return self.subscription