# # Form Images
# from io import BytesIO
# from os import name
# from PIL import Image
# from django.core.files import File
# from vendor.models import Vendor

from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55)
    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55)
    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    quantity = models.IntegerField(default=None)

    class Meta:
        ordering = ['-added_date']

    def __str__(self):
        return self.title

class rating(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    def __str__(self):
        return f"{self.rating}" 

class comment(models.Model):
    comment_name = models.CharField(max_length=255)
    comment_content = models.CharField(max_length=255)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_parent_id = models.IntegerField(null=False, default=None)
    def __str__(self):
        return f"{self.comment_name},{self.comment_content},{self.comment_parent}" 

