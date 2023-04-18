from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile
from django import forms


from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'company')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'company')
