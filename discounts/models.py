from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

User = get_user_model()

class PromoCode(models.Model):
    DISCOUNT_TYPE_CHOICES = [
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed Amount'),
    ]
    
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    minimum_order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    maximum_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    usage_limit = models.PositiveIntegerField(null=True, blank=True, help_text="Leave blank for unlimited usage")
    usage_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.code
    
    def is_valid(self):
        now = timezone.now()
        return (
            self.is_active and
            self.valid_from <= now <= self.valid_until and
            (self.usage_limit is None or self.usage_count < self.usage_limit)
        )
    
    def calculate_discount(self, order_amount):
        if not self.is_valid() or order_amount < self.minimum_order_amount:
            return 0
        
        if self.discount_type == 'percentage':
            discount = order_amount * (self.discount_value / 100)
        else:
            discount = self.discount_value
        
        if self.maximum_discount_amount:
            discount = min(discount, self.maximum_discount_amount)
        
        return discount

class SukiDiscount(models.Model):
    """Configuration for Suki (loyal customer) discounts"""
    name = models.CharField(max_length=100)
    minimum_orders = models.PositiveIntegerField(help_text="Minimum number of orders to qualify")
    discount_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['minimum_orders']
    
    def __str__(self):
        return f"{self.name} - {self.discount_percentage}% (≥{self.minimum_orders} orders)"

class FirstTimeCustomerPromo(models.Model):
    """Configuration for first-time customer promotions"""
    name = models.CharField(max_length=100)
    discount_type = models.CharField(max_length=20, choices=PromoCode.DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    minimum_order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    maximum_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def is_valid(self):
        now = timezone.now()
        return self.is_active and self.valid_from <= now <= self.valid_until
    
    def calculate_discount(self, order_amount):
        if not self.is_valid() or order_amount < self.minimum_order_amount:
            return 0
        
        if self.discount_type == 'percentage':
            discount = order_amount * (self.discount_value / 100)
        else:
            discount = self.discount_value
        
        if self.maximum_discount_amount:
            discount = min(discount, self.maximum_discount_amount)
        
        return discount

class DiscountUsage(models.Model):
    """Track discount usage by users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE, null=True, blank=True)
    discount_type = models.CharField(max_length=50)  # 'promo_code', 'suki', 'first_time'
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    used_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.discount_type} - ₱{self.discount_amount}"
