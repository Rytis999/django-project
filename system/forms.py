from django.forms import ModelForm
 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Product

class CreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']






class ProductForm(forms.ModelForm):
 

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'phone', 'image']
  
 
 





class CategoryFilterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category']



# class CategoryFilterForm(forms.Form):
#     category = forms.ChoiceField(
#         choices=[('', 'All Categories')] + [(category, category) for category in Product.objects.values_list('category', flat=True).distinct()],
#         required=False,
#         label='Filter by category'
#     )
