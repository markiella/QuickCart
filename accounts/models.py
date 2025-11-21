from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('staff', 'Staff'),
        ('rider', 'Rider'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    is_first_time_customer = models.BooleanField(default=True)
    suki_points = models.IntegerField(default=0)
    total_orders = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def is_suki_customer(self):
        """Check if customer qualifies for suki discount (3+ orders)"""
        return self.total_orders >= 3
    
    def get_suki_discount_percentage(self):
        """Calculate suki discount percentage based on order history"""
        if self.total_orders >= 10:
            return 15  # 15% for loyal customers
        elif self.total_orders >= 5:
            return 10  # 10% for regular customers
        elif self.total_orders >= 3:
            return 5   # 5% for suki customers
        return 0
