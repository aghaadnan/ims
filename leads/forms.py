from django import forms
from .models import SalesLead

class SalesLeadForm(forms.ModelForm):
    class Meta:
        model = SalesLead
        fields = ['cutomername', 'ContactNumber', 'Address', 'city', 'province', 'package', 'requirements', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
