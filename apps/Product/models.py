from django.db import models
from django.contrib.auth.models import User

# The Product model represents individual products in your store.
class Product(models.Model):
    name = models.CharField(max_length=200) # The name of the product.
    description = models.TextField() # The description of the product.
    price = models.DecimalField(max_digits=6, decimal_places=2) # The price of the product.
    image = models.ImageField(upload_to='products/images') # The image of the product, uploaded to the specified directory.

# The Category model represents different categories that products can belong to.
class Category(models.Model):
    name = models.CharField(max_length=200) # The name of the category.
    description = models.TextField() # The description of the category.
    image = models.ImageField(upload_to='category/images/') # The image of the category, uploaded to the specified directory.

# The Review model represents user reviews for products.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # The user who wrote the review. ForeignKey creates a many-to-one relationship.
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # The product that the review is for. ForeignKey creates a many-to-one relationship.
    rating = models.IntegerField() # The rating given by the user.
    review_text = models.TextField() # The text of the review.
