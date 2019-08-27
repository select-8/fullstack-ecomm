from django.db import models
from products.models import Product

# Create your models here.
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
    rating = models.IntegerField(choices=RATING_CHOISES, blank=True)

    def __str__(self):
        return self.comment