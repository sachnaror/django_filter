# project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filter/', include('filter.urls')),  # Ensure this line is correct
]
