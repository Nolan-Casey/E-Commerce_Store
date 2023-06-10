from django.db import models
from django.contrib.auth.models import User
from apps.Product.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    
class OrderType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.ImageField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
class Adress(models.Model):
    user = models.ForeignObject(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=25)
    
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
      