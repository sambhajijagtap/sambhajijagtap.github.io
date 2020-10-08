from django.db import models
from django.core.exceptions import ValidationError


def cost_value_greater_than_zero(value):
    if value < 0:
        raise ValidationError('Value of cost per item should be greater than or equal to zero.')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost_per_item = models.FloatField(default=0, validators=[cost_value_greater_than_zero, ])
    stock_quantity = models.PositiveIntegerField(default=0)
    volume = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if (self.cost_per_item > 0) and (self.stock_quantity > 0):
            self.volume = self.cost_per_item * self.stock_quantity
        else:
            self.volume = 0
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Products'
