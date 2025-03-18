from django.db import models
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name