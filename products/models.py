from __future__ import unicode_literals

from django.db import models
from clients.models import Client

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)

class Favourite(models.Model):
    user = models.ForeignKey(Client)
    product = models.ForeignKey(Product)


    def __str__(self):
        return '%s %s' % (self.user.name,  self.product.name)    
    class Meta:
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'
