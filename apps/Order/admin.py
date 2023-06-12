from django.contrib import admin
from .models import Order, OrderItem, Address, Payment, UserProfile

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'date_ordered', 'is_complete', 'transaction_id')
    list_filter = ('is_complete',)
    inlines = [OrderItemInline, PaymentInline]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'city', 'state', 'country', 'postal_code')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'amount', 'payment_method', 'date')