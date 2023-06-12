# This code defines three models for an online store: Product, Category, and Review. The Product 
# model includes fields for name, description, price, and image. The Category model includes 
# fields for name, description, and image. The Review model includes fields for the user 
# who wrote the review (linked to the built-in User model), the product being 
# reviewed (linked to the Product model), the rating given by the user, and the text 
# of the review. These models can be used to build a functional e-commerce 
# website with the ability for users to browse products, leave reviews, and purchase items.

# Import necessary modules
from django.db import models
from django.contrib.auth.models import User
 
# The Product model represents individual products in your store.
class Product(models.Model):
    # The name of the product.
    name = models.CharField(max_length=200)
    # The description of the product.
    description = models.TextField()
    # The price of the product.
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # The image of the product, uploaded to the specified directory.
    image = models.ImageField(upload_to='products/images')
 
 # The Category model represents different categories that products can belong to.
class Category(models.Model):
    # The name of the category.
    name = models.CharField(max_length=200)
    # The description of the category.
    description = models.TextField()
    # The image of the category, uploaded to the specified directory.
    image = models.ImageField(upload_to='category/images/')
 
# The Review model represents user reviews for products.
class Review(models.Model):
    # The user who wrote the review. ForeignKey creates a many-to-one relationship.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # The product that the review is for. ForeignKey creates a many-to-one relationship.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # The rating given by the user.
    rating = models.IntegerField()
    # The text of the review.
    review_text = models.TextField()