from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.category


class Kind(models.Model):
    kind = models.CharField(max_length=80, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.kind


class Brand(models.Model):
    name = models.CharField(max_length=254, default='')
    category = models.ForeignKey(Category, default='', on_delete=models.SET_DEFAULT)


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
