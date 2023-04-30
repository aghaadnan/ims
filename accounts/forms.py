from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile, ContactNumber, UserDocument
from django.forms import inlineformset_factory
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

class ContactNumberForm(forms.ModelForm):
    class Meta:
        model = ContactNumber
        fields = ('number',)

class UserDocumentForm(forms.ModelForm):
    class Meta:
        model = UserDocument
        fields = ('document',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'is_admin', 'is_agent', 'company', 'usertype')

# Create inline formsets for ContactNumber and UserDocument
ContactNumberFormSet = inlineformset_factory(UserProfile, ContactNumber, form=ContactNumberForm, extra=1, can_delete=True)
UserDocumentFormSet = inlineformset_factory(UserProfile, UserDocument, form=UserDocumentForm, extra=1, can_delete=True)