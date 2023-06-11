from django.contrib import admin
from .models import Order
from .models import OrderType
from .models import Address
from .models import Payment


class OrderAdmin(admin.OrderAdmin):
    list_display = ("data_order", "complete", "transaction_id")
    
class OrderTypeAdmin(admin.OrderTypeAdmin):
    list_display = ("quantity", "data_added")
    
class AddressAdmin(admin.AddressAdmin):
    list_display = ("street", "city", "state")
 
class PaymentAdmin(admin.PaymentAdmin):
    list_display = ("amount", "date")   

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderType, OrderTypeAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Payment, PaymentAdmin)



