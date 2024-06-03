import django_filters 

from .models import Product


class ProductFilter(django_filters.FilterSet):
    model = Product
    fields = ['category']



