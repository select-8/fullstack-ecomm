from django.test import TestCase
from .models import Product, Category

# Create your tests here.
class ProductTest(TestCase):
    
    '''
    Here we will define the tests
    that we will run against out Product models
    '''

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')

    
