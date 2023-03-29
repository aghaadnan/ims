from django import forms
from .models import Inventory, TrackerDevice


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'quantity', 'price']


class TrackerDeviceForm(forms.ModelForm):
    class Meta:
        model = TrackerDevice
        fields = ['model_number', 'vendor', 'price', 'imei']