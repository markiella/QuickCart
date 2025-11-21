from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('', views.order_list, name='order_list'),
    path('<uuid:order_id>/', views.order_detail, name='order_detail'),
    path('staff/', views.staff_order_list, name='staff_order_list'),
    path('staff/<uuid:order_id>/', views.staff_order_detail, name='staff_order_detail'),
]
