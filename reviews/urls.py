from django.urls import path
from .views import add_a_review

urlpatterns = [
    path('<int:product_id>/add_a_review', add_a_review, name='add_a_review'),
    ]




