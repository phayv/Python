from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    description = models.TextField()
    cost = models.FloatField()

    def __str__(self):
        return self.name
