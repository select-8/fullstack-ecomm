from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOISES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    # user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=254, default='')
    rating = models.IntegerField(choices=RATING_CHOISES, default=0)

    def __str__(self):
        return self.comment