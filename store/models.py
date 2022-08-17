from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    price = models.IntegerField()

# Create your models here.
class Product(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}- {self.last_name}- {self.price}"

    class Meta:
        ordering = ['price']
        verbose_name_plural = "Products"