from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

    class Meta:
       verbose_name_plural = 'categories'




class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50 )

    def __str__(self):
        return f'{self.name}'  
 


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0,decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length = 250, default= '' , blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    
    def __str__(self):
        return self.name




 