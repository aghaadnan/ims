from django import forms
from .models import Inventory, TrackerDevice, Sim
import csv
import io
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'quantity', 'price']


# class TrackerDeviceForm(forms.ModelForm):
#     class Meta:
#         model = TrackerDevice
#         fields = ['model_number', 'vendor', 'price', 'imei']


# class TrackerDeviceForm(forms.ModelForm):
#     class Meta:
#         model = TrackerDevice
#         fields = ('model_number', 'vendor', 'price', 'quantity', 'imei')
#         widgets = {
#             'imei': forms.FileInput(attrs={'accept': '.csv'}),
#         }

#     model_number = forms.CharField(max_length=255)
#     vendor = forms.CharField(max_length=255)
#     price = forms.DecimalField(decimal_places=2, max_digits=10)
#     quantity = forms.IntegerField(min_value=1)

#     def clean_imei(self):
#         imei_file = self.cleaned_data.get('imei', False)
#         if not imei_file:
#             raise forms.ValidationError('IMEI CSV file is required.')
#         try:
#             csv_file = io.StringIO(imei_file.read().decode())
#             reader = csv.reader(csv_file)
#             imeis = []
#             for row in reader:
#                 imeis.extend(row)
#         except Exception:
#             raise forms.ValidationError('Invalid CSV file.')
#         if len(set(imeis)) != self.cleaned_data['quantity']:
#             raise forms.ValidationError('The number of IMEIs in the CSV file must be equal to the quantity.')
#         return imeis
from django import forms
from django.core.validators import FileExtensionValidator

class TrackerDeviceForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)
    csv_file = forms.FileField(
        validators=[FileExtensionValidator(['csv'])],
        help_text='Please upload a CSV file containing IMEI numbers.'
    )

    class Meta:
        model = TrackerDevice
        fields = ('model_number', 'quantity', 'csv_file')
class SimForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)
    csv_file = forms.FileField(
        validators=[FileExtensionValidator(['csv'])],
        help_text='Please upload a CSV file containing IMEI numbers.'
    )

    class Meta:
        model = Sim
        fields = ['MSISDN', 'ICC_ID', 'OPERATOR', 'SIM_TYPE', 'PACKAGE', 'quantity', 'csv_file']
        #fields = ('model_number', 'vendor', 'price', )
