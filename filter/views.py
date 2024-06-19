# products/views.py

from django_filters.views import FilterView

from .filters import ProductFilter
from .models import Product


class ProductListView(FilterView):
    model = Product
    template_name = 'product/product_list.html'  # Ensure this path is correct
    paginate_by = 10
    filterset_class = ProductFilter
