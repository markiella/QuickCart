from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('api/get/', views.get_notifications, name='get_notifications'),
    path('api/mark-read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    path('login-alerts/', views.get_login_notifications, name='login_alerts'),
]
