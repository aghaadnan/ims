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
    datetime = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.subscription
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class CustomerGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Insurance(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='insurance_cities')
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='bank_cities')
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class VehicleMake(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class VehicleModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    vehiclemake = models.ForeignKey(VehicleMake, on_delete=models.CASCADE, related_name='vehicle_make')
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name


class Package(models.Model):
    package = models.CharField(max_length=255)
    days = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.package

class ComplainTypes(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name