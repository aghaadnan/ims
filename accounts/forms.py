from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile
from django import forms
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'company')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'company')
