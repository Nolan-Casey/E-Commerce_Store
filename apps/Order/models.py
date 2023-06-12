# This code defines several Django models related to an e-commerce order management 
# system. The models include Order, OrderItem, Address, Payment, and UserProfile.
#  1. Order Model:
# - Represents an order placed by a user.
# - Fields include user (foreign key to the User model), date_ordered, 
#   is_complete (boolean), and transaction_id.
# - Orders are sorted in descending order by date_ordered.
#  2. OrderItem Model:
# - Represents an individual item within an order.
# - Fields include product (foreign key to the Product model), 
#   order (foreign key to the Order model), quantity, and date_added.
# - OrderItems are sorted by the order they are added.
#  3. Address Model:
# - Represents a user's address.
# - Fields include user (foreign key to the User model), street_address, 
#   city, state, country, and postal_code.
# - Addresses are sorted by the user they belong to.
#  4. Payment Model:
# - Represents a payment made by a user for an order.
# - Fields include user (foreign key to the User model), order 
#   (foreign key to the Order model), amount, payment_method (with choices: credit_card, paypal, 
#   and cash), and date.
# - Payments are sorted in descending order by date.
# - The save method is overridden to handle custom validation.
#  5. UserProfile Model:
# - Represents a user's profile.
# - Fields include user (one-to-one field to the User model) and address 
#   (foreign key to the Address model).
# - UserProfiles are sorted by the user they belong to.
#   The code also includes several meta options and methods for each model, 
#   such as string representations, and verbose names.

# # Import necessary libraries and modules
from decimal import Decimal
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from apps.Product.models import Product

# Define the Order model
class Order(models.Model):
    # Define fields for the Order model
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="orders"
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, blank=True, unique=True)

    # Define meta options for the Order model
    class Meta:
        verbose_name_plural = "Orders"
        ordering = ("-date_ordered",)

    # Define string representation of the Order model
    def __str__(self):
        return f"Order {self.pk} by {self.user.username}"

# Define the OrderItem model
class OrderItem(models.Model):
    # Define fields for the OrderItem model
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="order_items"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items"
    )
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )
    date_added = models.DateTimeField(auto_now_add=True)

    # Define meta options for the OrderItem model
    class Meta:
        verbose_name_plural = "Order Items"

    # Define string representation of the OrderItem model
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.pk}"

# Define the Address model
class Address(models.Model):
    # Define fields for the Address model
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="addresses"
    )
    street_address = models.CharField(
        max_length=250, validators=[RegexValidator(r"^[0-9a-zA-Z\s]+$")], blank=True
    )
    city = models.CharField(
        max_length=100, validators=[RegexValidator(r"^[a-zA-Z\s]+$")], blank=True
    )
    state = models.CharField(
        max_length=25, validators=[RegexValidator(r"^[a-zA-Z\s]+$")], blank=True
    )
    country = models.CharField(
        max_length=100, validators=[RegexValidator(r"^[a-zA-Z\s]+$")], blank=True
    )
    postal_code = models.CharField(
        max_length=10, validators=[RegexValidator(r"^[0-9]+$")], blank=True
    )

    # Define meta options for the Address model
    class Meta:
        verbose_name_plural = "Addresses"
        ordering = ("user",)

    # Define string representation of the Address model
    def __str__(self):
        return f"{self.user.username}'s address"

# Define the Payment model
class Payment(models.Model):
    # Define choices for the payment_method field
    PAYMENT_METHOD_CHOICES = (
        ("credit_card", "Credit Card"),
        ("paypal", "PayPal"),
        ("cash", "Cash"),
    )

    # Define fields for the Payment model
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="payments"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="payments"
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    payment_method = models.CharField(
        max_length=100, choices=PAYMENT_METHOD_CHOICES
    )
    date = models.DateField(auto_now_add=True)

    # Define meta options for the Payment model
    class Meta:
        verbose_name_plural = "Payments"
        ordering = ("-date",)

    # Override the save method to handle custom validation
    def save(self, *args, **kwargs):
        if not self.pk:
            self.amount = round(self.amount, 2)
            if self.amount < 0:
                raise ValueError("Payment amount cannot be negative.")
        super().save(*args, **kwargs)

    # Define string representation of the Payment model
    def __str__(self):
        return f"{self.amount} paid by {self.user.username} for order {self.order.pk}"

# Define the UserProfile model
class UserProfile(models.Model):
    # Define fields for the UserProfile model
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )

    # Define meta options for the UserProfile model
    class Meta:
        verbose_name_plural = "User Profiles"

    # Define string representation of the UserProfile model
    def __str__(self):
        return self.user.username