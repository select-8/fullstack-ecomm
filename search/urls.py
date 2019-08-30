from django.urls import path
from .views import do_search, cat_filter

urlpatterns = [
    path('', do_search, name='search'),
    path('', cat_filter, name='cat_filter'),
    ]