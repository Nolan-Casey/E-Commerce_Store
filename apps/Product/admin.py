# Import necessary modules and models
from django.contrib import admin
from .models import Product, Category, Review

# Define ProductAdmin class with list_display, search_fields, list_filter, and ordering attributes
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # columns to display in list view
    search_fields = ('name',)  # fields to search in the search bar
    list_filter = ('price',)  # fields to filter the list view
    ordering = ('name',)  # order the list view by name

# Define CategoryAdmin class with list_display attribute
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') # columns to display in list view

# Define ReviewAdmin class with list_display attribute
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'review_text')

# Register models with their respective admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)