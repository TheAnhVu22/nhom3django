from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default=None)
    password = models.CharField(max_length=50, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    # def get_balance(self):
    #     items = self.items.filter(vendor_paid=False, order__vendors__in=[self.id])
    #     return sum((item.product.price * item.quantity) for item in items)

    # def get_paid_amount(self):
    #     items = self.items.filter(vendor_paid=True, order__vendors__in=[self.id])
    #     return sum((item.product.price * item.quantity) for item in items)

