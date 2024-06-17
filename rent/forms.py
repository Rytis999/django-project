from .models import Car
from django import forms

class carRentForm(forms.ModelForm):
 

    class Meta:
        model = Car
        fields = ['name',  'price_per_day', 'description',    'phone', 'image']
  
 
 
