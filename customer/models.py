from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name},{self.email},{self.password}" 
