from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=115)
    product_price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=255)
    product_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
