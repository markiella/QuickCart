from django.contrib import admin
from .models import Order, OrderItem, OrderStatusHistory

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_name', 'product_price', 'total_price')

class OrderStatusHistoryInline(admin.TabularInline):
    model = OrderStatusHistory
    extra = 0
    readonly_fields = ('created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'total_amount', 'payment_method', 'assigned_staff', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at', 'assigned_staff')
    search_fields = ('order_number', 'user__username', 'customer_name', 'customer_email')
    readonly_fields = ('id', 'order_number', 'created_at', 'updated_at')
    inlines = [OrderItemInline, OrderStatusHistoryInline]
    
    fieldsets = (
        ('Order Information', {
            'fields': ('id', 'order_number', 'user', 'status', 'assigned_staff')
        }),
        ('Customer Information', {
            'fields': ('customer_name', 'customer_email', 'customer_phone', 'delivery_address')
        }),
        ('Payment & Pricing', {
            'fields': ('payment_method', 'subtotal', 'discount_amount', 'delivery_fee', 'total_amount')
        }),
        ('Discount Information', {
            'fields': ('discount_type', 'discount_code')
        }),
        ('Additional Information', {
            'fields': ('notes', 'created_at', 'updated_at', 'delivered_at')
        }),
    )

@admin.register(OrderStatusHistory)
class OrderStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'changed_by', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order__order_number', 'changed_by__username')
