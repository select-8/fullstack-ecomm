import django_filters
from django_filters import ModelChoiceFilter
from .models import Product, Category, Kind

class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Category
        fields = ['kind']
