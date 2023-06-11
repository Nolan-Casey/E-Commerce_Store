from django.contrib import admin
from .models import Product
from .models import Category
from .models import Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # columns to display in list view
    search_fields = ('name',)  # fields to search in the search bar
    list_filter = ('price',)  # fields to filter the list view
    ordering = ('name',)  # order the list view by name
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') # columns to display in list view
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'review_text')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product,ProductAdmin)


