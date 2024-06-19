# filters.py

import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'title': ['icontains'],
            'price': ['gte', 'lte'],
            'featured': ['exact'],
            'created_at': ['date__gte', 'date__lte'],
        }
