from django import forms
from products.models import Product
from .models import Review
from django.contrib import admin

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ('comment', 'rating')

#         comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20})


class ReviewForm( forms.ModelForm ):
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    rating = forms.NumberInput()

    class Meta:
        model = Review
        fields = ('comment', 'rating')

class Cab_Admin( admin.ModelAdmin ):
    form = ReviewForm