from django.test import TestCase
from .models import Product


class ProductModelTestCase(TestCase):
    def test_volume_generated_automatically(self):
        # Product object created without assigning value to volume. It will generated automatically.
        prod = Product.objects.create(name='Laptop', description='1TB HDD', cost_per_item=30000.0, stock_quantity=2)
        self.assertEqual(prod.volume, (prod.cost_per_item * prod.stock_quantity))
        print('Test 1 completed')

    def test_volume_zero_as_cost_per_item_zero(self):
        prod = Product.objects.create(name='Laptop', description='1TB HDD', cost_per_item=0.0, stock_quantity=5)
        self.assertEqual(prod.volume, 0)
        print('Test 2 completed')

    def test_volume_zero_as_stock_quantity_zero(self):
        prod = Product.objects.create(name='Laptop', description='1TB HDD', cost_per_item=40000.0, stock_quantity=0)
        self.assertEqual(prod.volume, 0)
        print('Test 3 completed')

    def test_volume_zero_as_cost_per_item_and_stock_quantity_zero(self):
        prod = Product.objects.create(name='Laptop', description='1TB HDD', cost_per_item=0.0, stock_quantity=0)
        self.assertEqual(prod.volume, 0)
        print('Test 4 completed')
