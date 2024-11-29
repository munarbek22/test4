from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'manufacturer', 'price', 'release_date', 'image', 'category', 'features']