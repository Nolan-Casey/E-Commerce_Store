from django.contrib import admin
from .models import Product
from .models import Category
from .models import Review

class ProductAdmin(admin.ProductAdmin):
    list_display = ("name", "description", "price", "image")
    
class CategoryAdmin(admin.CategoryAdmin):
    list_display = ("name", "description", "image")
    
class ReviewAdmin(admin.ReviewAdmin):
    list_display = ("rating", "review_text")

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product,ProductAdmin)


