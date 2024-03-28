from django.db import models

# Create your models here.
class Product(models.Model):
    serial_number = models.CharField(max_length=50, primary_key=True)
    product_name = models.CharField(max_length=200, blank=False, default=None)
    product_desc = models.CharField(max_length=2000, blank=False, default=None)
    manufacturer_info = models.CharField(max_length=500, blank=False, default=None)
    warranty_info = models.CharField(max_length=200, null=True)
    date_of_manufacture = models.DateField(blank=False, default=None)
