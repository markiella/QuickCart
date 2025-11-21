from .models import Category

def categories_context(request):
    """Add categories to all templates"""
    return {
        'categories': Category.objects.filter(is_active=True).order_by('name')
    }
