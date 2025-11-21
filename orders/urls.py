from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('', views.order_list, name='order_list'),
    path('<uuid:order_id>/', views.order_detail, name='order_detail'),
    path('<uuid:order_id>/edit/', views.edit_order, name='edit_order'),
    path('<uuid:order_id>/delete/', views.delete_order, name='delete_order'),
    path('staff/', views.staff_order_list, name='staff_order_list'),
    path('staff/<uuid:order_id>/', views.staff_order_detail, name='staff_order_detail'),
]
