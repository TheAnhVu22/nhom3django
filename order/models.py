from django.db import models
from product.models import Product
from vendor.models import Vendor

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=100,default=None)
    last_name = models.CharField(max_length=100,default=None) 
    email = models.CharField(max_length=100,default=None)
    address = models.CharField(max_length=100,default=None)
    zipcode = models.CharField(max_length=100,default=None)
    place = models.CharField(max_length=100,default=None)
    phone = models.CharField(max_length=100,default=None) 
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2,default=None)
    vendors = models.CharField(max_length=100,default=None)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE,default=None)
    vendor = models.CharField(max_length=100,default=None)
    vendor_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2,default=None)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        return self.price * self.quantity
