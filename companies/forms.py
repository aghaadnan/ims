from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_bootstrap5.bootstrap5 import BS5Accordion
from .models import Company

class CompanyForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Save'))
    class Meta:
        model = Company
        fields = ['name', 'contactperson', 'address', 'phone','city','email','GST','NTN','package']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        # self.fields['city'].widget = forms.Select(attrs={'class': 'form-control'})
        # self.fields['address'].widget = forms.TextInput(attrs={'class': 'form-control'})