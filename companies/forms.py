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
        fields = ['name', 'address', 'phone']
