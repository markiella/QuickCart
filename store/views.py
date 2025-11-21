from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from .models import Product, Category

def landing_page(request):
    """Landing page view"""
    # Redirect admin users to dashboard
    if request.user.is_authenticated and request.user.role == 'admin':
        from django.shortcuts import redirect
        return redirect('dashboard:home')
    
    categories = Category.objects.filter(is_active=True)[:8]  # Show first 8 categories
    featured_products = Product.objects.filter(
        is_available=True, 
        is_featured=True
    )[:8]  # Show 8 featured products
    
    context = {
        'categories': categories,
        'featured_products': featured_products,
    }
    return render(request, 'landing.html', context)

def product_list(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.filter(is_active=True)
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug, is_active=True)
        products = products.filter(category=category)
    else:
        category = None
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
    
    # Sort functionality
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'newest':
        products = products.order_by('-created_at')
    else:
        products = products.order_by('name')
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Featured products for homepage
    featured_products = Product.objects.filter(is_featured=True, is_available=True)[:6]
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category,
        'search_query': search_query,
        'sort_by': sort_by,
        'featured_products': featured_products,
    }
    
    return render(request, 'store/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    related_products = Product.objects.filter(
        category=product.category, 
        is_available=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    
    return render(request, 'store/product_detail.html', context)

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = Product.objects.filter(category=category, is_available=True)
    
    # Sort functionality
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'newest':
        products = products.order_by('-created_at')
    else:
        products = products.order_by('name')
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
        'sort_by': sort_by,
    }
    
    return render(request, 'store/category_products.html', context)

def live_search(request):
    """AJAX live search endpoint"""
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        query = request.GET.get('q', '').strip()
        category_slug = request.GET.get('category', '')
        
        if len(query) < 2:  # Only search if query is at least 2 characters
            return JsonResponse({'results': []})
        
        # Base queryset
        products = Product.objects.filter(is_available=True)
        
        # Filter by category if specified
        if category_slug:
            try:
                category = Category.objects.get(slug=category_slug, is_active=True)
                products = products.filter(category=category)
            except Category.DoesNotExist:
                pass
        
        # Search in name and description
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).distinct()[:10]  # Limit to 10 results for performance
        
        # Format results
        results = []
        for product in products:
            # Get product emoji icon
            product_icon = '📦'  # default
            name_lower = product.name.lower()
            if 'tomato' in name_lower:
                product_icon = '🍅'
            elif 'lettuce' in name_lower:
                product_icon = '🥬'
            elif 'onion' in name_lower:
                product_icon = '🧅'
            elif 'carrot' in name_lower:
                product_icon = '🥕'
            elif 'potato' in name_lower:
                product_icon = '🥔'
            elif 'banana' in name_lower:
                product_icon = '🍌'
            elif 'apple' in name_lower:
                product_icon = '🍎'
            elif 'orange' in name_lower:
                product_icon = '🍊'
            elif 'mango' in name_lower:
                product_icon = '🥭'
            elif 'chip' in name_lower:
                product_icon = '🍟'
            elif 'water' in name_lower:
                product_icon = '💧'
            elif 'cola' in name_lower:
                product_icon = '🥤'
            elif 'juice' in name_lower:
                product_icon = '🧃'
            elif 'tea' in name_lower:
                product_icon = '🧋'
            elif 'chicken' in name_lower:
                product_icon = '🍗'
            elif 'beef' in name_lower:
                product_icon = '🥩'
            elif 'rice' in name_lower:
                product_icon = '🍚'
            elif 'egg' in name_lower:
                product_icon = '🥚'
            elif 'milk' in name_lower:
                product_icon = '🥛'
            elif 'cheese' in name_lower:
                product_icon = '🧀'
            elif 'oil' in name_lower:
                product_icon = '🫒'
            elif 'sugar' in name_lower:
                product_icon = '🍯'
            
            results.append({
                'id': product.id,
                'name': product.name,
                'price': str(product.price),
                'unit': product.unit,
                'category': product.category.name,
                'slug': product.slug,
                'icon': product_icon,
                'stock_status': product.get_stock_status(),
                'image_url': product.image.url if product.image else None,
            })
        
        return JsonResponse({'results': results})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
