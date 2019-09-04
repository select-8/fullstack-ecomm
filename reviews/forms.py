from django import forms
from products.models import Product
from .models import Review
from django.contrib import admin
from django.forms import widgets
from django.forms.widgets import RadioSelect





class ReviewForm( forms.ModelForm ):
    RATING_CHOISES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    comment = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    rating = forms.ChoiceField(choices=RATING_CHOISES)

    class Meta:
        model = Review
        fields = ('comment', 'rating')

class Cab_Admin( admin.ModelAdmin ):
    form = ReviewForm