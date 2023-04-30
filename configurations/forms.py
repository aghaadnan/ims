from django import forms
from .models import (
    Subscriptions, Department, 
    Package, ComplainTypes, 
    VehicleMake, VehicleModel, 
    Province, CustomerGroup, Insurance, Bank
)


class SubscriptionsForm(forms.ModelForm):
    
    class Meta:
        model = Subscriptions
        fields = ['subscription', 'days', 'price']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']
        def __init__(self, *args, **kwargs):
            super(DepartmentForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                # Add a custom class for inputs
                self.fields[field].widget.attrs.update({'class': 'form-control'})

                # Add a custom class for the label only if the field name is 'name'
                if field == 'name':
                    self.fields[field].label = forms.Label(attrs={'class': 'form-label'}, label=self.fields[field].label)
        
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomerGroupForm(forms.ModelForm):
    class Meta:
        model = CustomerGroup
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InsuranceForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = ['name', 'description', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'description', 'city']

    def __init__(self, *args, **kwargs):
        super(BankForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class VehicleMakeForm(forms.ModelForm):
    class Meta:
        model = VehicleMake
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = ['name', 'description', 'vehiclemake']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'vehiclemake': forms.Select(attrs={'class': 'form-control'}),
        }

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['package', 'days', 'price']
        widgets = {
            'package': forms.TextInput(attrs={'class': 'form-control'}),
            'days': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ComplainTypesForm(forms.ModelForm):
    class Meta:
        model = ComplainTypes
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})