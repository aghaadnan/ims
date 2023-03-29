from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company

class UserType(models.Model):
    MANAGER = 1
    AGENT = 2
    OPERATOR = 3
    TYPE_CHOICES = (
        (MANAGER, 'Manager'),
        (AGENT, 'Agent'),
        (OPERATOR, 'Installer')
    )
    id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, primary_key=True)
    def __str__(self):
        return self.get_id_display()

class UserProfile(AbstractUser):
    is_manager  = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    is_installer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='owned_companies')
    #usertype = models.ManyToManyField(UserType)