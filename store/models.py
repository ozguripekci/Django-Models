from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    price = models.IntegerField()

YEAR_IN_SCHOOL_CHOICES = [
    ("FR", 'Freshman'),
    ("SP", 'Sophomore'),
    ("JR", 'Junior'),
    ("SR", 'Senior'),
    ("GRD", 'Graduate'),
]
class Product(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    price = models.IntegerField()
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='media/')
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    year_in_school = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES, default="FR")

    def __str__(self):
        return f"{self.first_name}- {self.last_name}- {self.price}"

    class Meta:
        ordering = ['price']
        verbose_name_plural = "Products"