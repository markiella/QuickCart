from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification

@login_required
def get_notifications(request):
    """Get unread notifications for the current user"""
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')[:5]
    
    data = {
        'count': notifications.count(),
        'notifications': [
            {
                'id': n.id,
                'title': n.title,
                'message': n.message,
                'type': n.notification_type,
                'created_at': n.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            }
            for n in notifications
        ]
    }
    
    return JsonResponse(data)

@login_required
def mark_as_read(request, notification_id):
    """Mark a notification as read"""
    try:
        notification = Notification.objects.get(id=notification_id, user=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({'status': 'success'})
    except Notification.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

@login_required
def get_login_notifications(request):
    """Get unread notifications for display on login"""
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    
    return render(request, 'notifications/login_alerts.html', {
        'notifications': notifications
    })
