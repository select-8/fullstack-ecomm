from django.urls import path, include, re_path
from .views import add_a_review


app_name = 'ratings'

urlpatterns = [
    path('<int:product_id>/add_a_review', add_a_review, name='add_a_review'),
    ]




