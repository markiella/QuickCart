from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('inventory/', views.inventory_management, name='inventory'),
    path('orders/', views.admin_orders, name='admin_orders'),
    path('get-order/<uuid:order_id>/', views.get_order_details, name='get_order_details'),
    path('update-order-status/<uuid:order_id>/', views.update_order_status, name='update_order_status'),
    path('assign-staff/<uuid:order_id>/', views.assign_staff, name='assign_staff'),
    path('update-stock/<int:product_id>/', views.update_stock, name='update_stock'),
    path('users/', views.user_management, name='user_management'),
    path('products/', views.product_management, name='product_management'),
    path('categories/', views.category_management, name='category_management'),
    path('promos/', views.promo_management, name='promo_management'),
    # AJAX Product Management
    path('add-product/', views.add_product, name='add_product'),
    path('get-product/<int:product_id>/', views.get_product, name='get_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
]
