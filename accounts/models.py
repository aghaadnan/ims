from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company

class UserType(models.Model):
    usertype = models.CharField(max_length=255)
    datentime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.usertype

class UserProfile(AbstractUser):
    # is_manager  = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    # is_installer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='owned_companies')
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True, related_name='owned_companies')