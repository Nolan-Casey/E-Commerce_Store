from django.db import models
from django.contrib.auth.models import User
from apps.Product.models import Product

# The Order model represents individual orders in your store.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who placed the order. ForeignKey creates a many-to-one relationship.
    data_order = models.DateTimeField(auto_now_add=True)  # The date and time when the order was placed, automatically set to the current date and time when an order is created.
    complete = models.BooleanField(default=False,null=True, blank=False)  # Whether the order is complete.
    transaction_id = models.CharField(max_length=200, null=True)  # The transaction ID for the order.

# The OrderType model represents the items within each order.
class OrderType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)  # The product in the order. ForeignKey creates a many-to-one relationship.
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)  # The order the product is part of. ForeignKey creates a many-to-one relationship.
    quantity = models.IntegerField(default=0, null=True, blank=True)  # The quantity of this product in the order.
    date_added = models.DateTimeField(auto_now_add=True)  # The date and time when this item was added to the order, automatically set to the current date and time when an item is added.

# The Address model represents the shipping addresses of users.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user this address belongs to. ForeignKey creates a many-to-one relationship.
    street = models.CharField(max_length=250)  # The street name and number of the address.
    city = models.CharField(max_length=100)  # The city of the address.
    state = models.CharField(max_length=25)  # The state of the address.

# The Payment model represents payments made by users.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who made the payment. ForeignKey creates a many-to-one relationship.
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # The order the payment is for. ForeignKey creates a many-to-one relationship.
    amount = models.DecimalField(max_digits=6, decimal_places=2)  # The amount of the payment.
    date = models.DateTimeField(auto_now_add=True)  # The date and time when the payment was made, automatically set to the current date and time when a payment is made.
