from django.contrib import admin
from .models import Contact, Product, Category, Order, OrderItem  # Import the models

# Register Contact, Product, and Category
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Category)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'email', 'total_amount', 'status', 'payment_status', 'created_at')
    list_filter = ('status', 'payment_status', 'created_at')
    search_fields = ('user__username', 'email', 'first_name', 'last_name')
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity',)