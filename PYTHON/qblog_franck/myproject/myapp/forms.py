from django import forms
from models import *

class AddHouseForm(forms.Form):
    
    coordinates = forms.CharField(max_length=200, required=True)
    owner = forms.CharField(max_length=100, required=True)
    price = forms.IntegerField(required=True)
    area = forms.IntegerField(required=True)

    def clean(self):
        cleaned_data = self.cleaned_data

        coordinates = cleaned_data.get("coordinates")
        owner = cleaned_data.get("owner")
        price = cleaned_data.get("price")
        area = cleaned_data.get("area")

        return cleaned_data