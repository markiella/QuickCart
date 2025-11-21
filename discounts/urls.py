from django.urls import path
from . import views

app_name = 'discounts'

urlpatterns = [
    path('apply-promo/', views.apply_promo_code, name='apply_promo_code'),
    path('promos/', views.promo_code_list, name='promo_list'),
]
