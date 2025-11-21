from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from store.models import Category, Product
from discounts.models import SukiDiscount, FirstTimeCustomerPromo, PromoCode
from django.utils import timezone
from datetime import timedelta
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample data for Quick Cart'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to seed database...'))
        
        # Create superuser
        self.create_users()
        
        # Create categories
        self.create_categories()
        
        # Create products
        self.create_products()
        
        # Create discount configurations
        self.create_discounts()
        
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))

    def create_users(self):
        self.stdout.write('Creating users...')
        
        # Create superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@quickcart.ph',
                password='admin123',
                first_name='Admin',
                last_name='User',
                role='admin'
            )
            self.stdout.write('  - Admin user created')
        
        # Create staff user
        if not User.objects.filter(username='staff').exists():
            User.objects.create_user(
                username='staff',
                email='staff@quickcart.ph',
                password='staff123',
                first_name='Staff',
                last_name='Member',
                role='staff',
                phone_number='+63 123 456 7890',
                address='Quick Cart Warehouse, Local Area'
            )
            self.stdout.write('  - Staff user created')
        
        # Create rider user
        if not User.objects.filter(username='rider').exists():
            User.objects.create_user(
                username='rider',
                email='rider@quickcart.ph',
                password='rider123',
                first_name='Delivery',
                last_name='Rider',
                role='rider',
                phone_number='+63 123 456 7891',
                address='Local Area'
            )
            self.stdout.write('  - Rider user created')
        
        # Create sample customers
        customers_data = [
            {
                'username': 'customer1',
                'email': 'customer1@example.com',
                'first_name': 'Juan',
                'last_name': 'Dela Cruz',
                'total_orders': 5,
                'is_first_time_customer': False
            },
            {
                'username': 'customer2',
                'email': 'customer2@example.com',
                'first_name': 'Maria',
                'last_name': 'Santos',
                'total_orders': 0,
                'is_first_time_customer': True
            }
        ]
        
        for customer_data in customers_data:
            if not User.objects.filter(username=customer_data['username']).exists():
                User.objects.create_user(
                    username=customer_data['username'],
                    email=customer_data['email'],
                    password='customer123',
                    first_name=customer_data['first_name'],
                    last_name=customer_data['last_name'],
                    role='customer',
                    phone_number='+63 987 654 3210',
                    address='Sample Address, Local Area',
                    total_orders=customer_data['total_orders'],
                    is_first_time_customer=customer_data['is_first_time_customer']
                )
                self.stdout.write(f'  - Customer {customer_data["username"]} created')

    def create_categories(self):
        self.stdout.write('Creating categories...')
        
        categories_data = [
            {
                'name': 'Fresh Vegetables',
                'description': 'Fresh and organic vegetables delivered daily'
            },
            {
                'name': 'Fruits',
                'description': 'Sweet and juicy fruits, locally sourced'
            },
            {
                'name': 'Snacks & Chips',
                'description': 'Delicious snacks and chips for every craving'
            },
            {
                'name': 'Beverages',
                'description': 'Refreshing drinks and beverages'
            },
            {
                'name': 'Ready-to-Eat Meals',
                'description': 'Convenient ready-made meals and dishes'
            },
            {
                'name': 'Dairy & Eggs',
                'description': 'Fresh dairy products and farm eggs'
            },
            {
                'name': 'Pantry Essentials',
                'description': 'Rice, oil, condiments and cooking essentials'
            }
        ]
        
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={
                    'slug': slugify(category_data['name']),
                    'description': category_data['description'],
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(f'  - Category "{category.name}" created')

    def create_products(self):
        self.stdout.write('Creating products...')
        
        # Get categories
        vegetables = Category.objects.get(name='Fresh Vegetables')
        fruits = Category.objects.get(name='Fruits')
        snacks = Category.objects.get(name='Snacks & Chips')
        beverages = Category.objects.get(name='Beverages')
        meals = Category.objects.get(name='Ready-to-Eat Meals')
        dairy = Category.objects.get(name='Dairy & Eggs')
        pantry = Category.objects.get(name='Pantry Essentials')
        
        products_data = [
            # Vegetables
            {'name': 'Fresh Tomatoes', 'category': vegetables, 'price': 45.00, 'description': 'Fresh red tomatoes, perfect for cooking and salads', 'stock': 50, 'unit': 'kg', 'featured': True, 'image_url': 'https://images.unsplash.com/photo-1546470427-e5ac89c8ba8e?w=400&h=300&fit=crop'},
            {'name': 'Green Lettuce', 'category': vegetables, 'price': 35.00, 'description': 'Crisp green lettuce leaves, great for salads', 'stock': 30, 'unit': 'head', 'image_url': 'https://images.unsplash.com/photo-1622206151226-18ca2c9ab4a1?w=400&h=300&fit=crop'},
            {'name': 'White Onions', 'category': vegetables, 'price': 40.00, 'description': 'Fresh white onions, cooking essential', 'stock': 40, 'unit': 'kg', 'image_url': 'https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=400&h=300&fit=crop'},
            {'name': 'Carrots', 'category': vegetables, 'price': 50.00, 'description': 'Sweet orange carrots, rich in vitamins', 'stock': 25, 'unit': 'kg', 'image_url': 'https://images.unsplash.com/photo-1445282768818-728615cc910a?w=400&h=300&fit=crop'},
            {'name': 'Potatoes', 'category': vegetables, 'price': 55.00, 'description': 'Fresh potatoes, versatile cooking ingredient', 'stock': 60, 'unit': 'kg', 'image_url': 'https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=400&h=300&fit=crop'},
            
            # Fruits
            {'name': 'Bananas', 'category': fruits, 'price': 60.00, 'description': 'Sweet ripe bananas, rich in potassium', 'stock': 40, 'unit': 'kg', 'featured': True, 'image_url': 'https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=400&h=300&fit=crop'},
            {'name': 'Red Apples', 'category': fruits, 'price': 120.00, 'description': 'Crisp red apples, imported quality', 'stock': 20, 'unit': 'kg', 'image_url': 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=400&h=300&fit=crop'},
            {'name': 'Oranges', 'category': fruits, 'price': 80.00, 'description': 'Juicy oranges, high in vitamin C', 'stock': 35, 'unit': 'kg', 'image_url': 'https://images.unsplash.com/photo-1547514701-42782101795e?w=400&h=300&fit=crop'},
            {'name': 'Mangoes', 'category': fruits, 'price': 150.00, 'description': 'Sweet Philippine mangoes, in season', 'stock': 15, 'unit': 'kg', 'image_url': 'https://images.unsplash.com/photo-1553279768-865429fa0078?w=400&h=300&fit=crop'},
            
            # Snacks
            {'name': 'Potato Chips - Original', 'category': snacks, 'price': 25.00, 'description': 'Crispy potato chips, original flavor', 'stock': 100, 'unit': 'pack', 'image_url': 'https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=400&h=300&fit=crop'},
            {'name': 'Corn Chips - Cheese', 'category': snacks, 'price': 30.00, 'description': 'Crunchy corn chips with cheese flavor', 'stock': 80, 'unit': 'pack', 'featured': True, 'image_url': 'https://images.unsplash.com/photo-1613919113640-25732ec5e61f?w=400&h=300&fit=crop'},
            {'name': 'Crackers', 'category': snacks, 'price': 35.00, 'description': 'Light and crispy crackers, perfect snack', 'stock': 60, 'unit': 'pack', 'image_url': 'https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=400&h=300&fit=crop'},
            
            # Beverages
            {'name': 'Bottled Water 500ml', 'category': beverages, 'price': 15.00, 'description': 'Pure drinking water, 500ml bottle', 'stock': 200, 'unit': 'bottle', 'image_url': 'https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=400&h=300&fit=crop'},
            {'name': 'Soft Drink - Cola', 'category': beverages, 'price': 25.00, 'description': 'Refreshing cola soft drink, 330ml', 'stock': 150, 'unit': 'can', 'image_url': 'https://images.unsplash.com/photo-1581636625402-29b2a704ef13?w=400&h=300&fit=crop'},
            {'name': 'Fresh Orange Juice', 'category': beverages, 'price': 45.00, 'description': 'Freshly squeezed orange juice, 250ml', 'stock': 30, 'unit': 'bottle', 'featured': True, 'image_url': 'https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=400&h=300&fit=crop'},
            {'name': 'Iced Tea', 'category': beverages, 'price': 20.00, 'description': 'Refreshing iced tea, lemon flavor', 'stock': 80, 'unit': 'bottle', 'image_url': 'https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&h=300&fit=crop'},
            
            # Ready-to-Eat Meals
            {'name': 'Chicken Adobo Meal', 'category': meals, 'price': 120.00, 'description': 'Traditional Filipino chicken adobo with rice', 'stock': 20, 'unit': 'pack', 'featured': True, 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400&h=300&fit=crop'},
            {'name': 'Beef Stew Meal', 'category': meals, 'price': 150.00, 'description': 'Hearty beef stew with vegetables and rice', 'stock': 15, 'unit': 'pack', 'image_url': 'https://images.unsplash.com/photo-1574484284002-952d92456975?w=400&h=300&fit=crop'},
            {'name': 'Fried Rice with Egg', 'category': meals, 'price': 80.00, 'description': 'Delicious fried rice with scrambled egg', 'stock': 25, 'unit': 'pack', 'image_url': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400&h=300&fit=crop'},
            {'name': 'Pancit Canton', 'category': meals, 'price': 90.00, 'description': 'Filipino stir-fried noodles with vegetables', 'stock': 30, 'unit': 'pack', 'image_url': 'https://images.unsplash.com/photo-1555126634-323283e090fa?w=400&h=300&fit=crop'},
            
            # Dairy & Eggs
            {'name': 'Fresh Milk 1L', 'category': dairy, 'price': 85.00, 'description': 'Fresh cow milk, 1 liter carton', 'stock': 40, 'unit': 'carton', 'image_url': 'https://images.unsplash.com/photo-1563636619-e9143da7973b?w=400&h=300&fit=crop'},
            {'name': 'Farm Fresh Eggs', 'category': dairy, 'price': 180.00, 'description': 'Fresh chicken eggs from local farms', 'stock': 50, 'unit': 'dozen', 'featured': True, 'image_url': 'https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?w=400&h=300&fit=crop'},
            {'name': 'Cheese Slices', 'category': dairy, 'price': 120.00, 'description': 'Processed cheese slices, perfect for sandwiches', 'stock': 25, 'unit': 'pack', 'image_url': 'https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?w=400&h=300&fit=crop'},
            
            # Pantry Essentials
            {'name': 'Jasmine Rice 5kg', 'category': pantry, 'price': 250.00, 'description': 'Premium jasmine rice, 5kg bag', 'stock': 30, 'unit': 'bag', 'image_url': 'https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400&h=300&fit=crop'},
            {'name': 'Cooking Oil 1L', 'category': pantry, 'price': 120.00, 'description': 'Pure cooking oil, 1 liter bottle', 'stock': 40, 'unit': 'bottle', 'image_url': 'https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=400&h=300&fit=crop'},
            {'name': 'Soy Sauce', 'category': pantry, 'price': 45.00, 'description': 'Premium soy sauce for cooking', 'stock': 60, 'unit': 'bottle', 'image_url': 'https://images.unsplash.com/photo-1599909533730-0b8b5b0b7b1a?w=400&h=300&fit=crop'},
            {'name': 'White Sugar 1kg', 'category': pantry, 'price': 65.00, 'description': 'Refined white sugar, 1kg pack', 'stock': 50, 'unit': 'pack', 'image_url': 'https://images.unsplash.com/photo-1587735243615-c03f25aaff15?w=400&h=300&fit=crop'},
        ]
        
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'slug': slugify(product_data['name']),
                    'category': product_data['category'],
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock_quantity': product_data['stock'],
                    'unit': product_data['unit'],
                    'is_available': True,
                    'is_featured': product_data.get('featured', False)
                }
            )
            if created:
                self.stdout.write(f'  - Product "{product.name}" created')

    def create_discounts(self):
        self.stdout.write('Creating discount configurations...')
        
        # Create Suki Discount tiers
        suki_discounts = [
            {'name': 'Bronze Suki', 'minimum_orders': 3, 'discount_percentage': 5.00},
            {'name': 'Silver Suki', 'minimum_orders': 5, 'discount_percentage': 10.00},
            {'name': 'Gold Suki', 'minimum_orders': 10, 'discount_percentage': 15.00},
        ]
        
        for suki_data in suki_discounts:
            suki, created = SukiDiscount.objects.get_or_create(
                name=suki_data['name'],
                defaults={
                    'minimum_orders': suki_data['minimum_orders'],
                    'discount_percentage': suki_data['discount_percentage'],
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(f'  - Suki discount "{suki.name}" created')
        
        # Create First-time Customer Promo
        first_time_promo, created = FirstTimeCustomerPromo.objects.get_or_create(
            name='Welcome Discount',
            defaults={
                'discount_type': 'percentage',
                'discount_value': 10.00,
                'minimum_order_amount': 200.00,
                'maximum_discount_amount': 100.00,
                'is_active': True,
                'valid_from': timezone.now(),
                'valid_until': timezone.now() + timedelta(days=365)
            }
        )
        if created:
            self.stdout.write('  - First-time customer promo created')
        
        # Create sample promo codes
        promo_codes = [
            {
                'code': 'WELCOME20',
                'description': 'Welcome discount for new customers',
                'discount_type': 'percentage',
                'discount_value': 20.00,
                'minimum_order_amount': 300.00,
                'maximum_discount_amount': 150.00
            },
            {
                'code': 'SAVE50',
                'description': 'Save 50 pesos on orders above 500',
                'discount_type': 'fixed',
                'discount_value': 50.00,
                'minimum_order_amount': 500.00
            },
            {
                'code': 'WEEKEND15',
                'description': 'Weekend special 15% off',
                'discount_type': 'percentage',
                'discount_value': 15.00,
                'minimum_order_amount': 250.00,
                'maximum_discount_amount': 100.00
            }
        ]
        
        for promo_data in promo_codes:
            promo, created = PromoCode.objects.get_or_create(
                code=promo_data['code'],
                defaults={
                    'description': promo_data['description'],
                    'discount_type': promo_data['discount_type'],
                    'discount_value': promo_data['discount_value'],
                    'minimum_order_amount': promo_data['minimum_order_amount'],
                    'maximum_discount_amount': promo_data.get('maximum_discount_amount'),
                    'usage_limit': 100,
                    'is_active': True,
                    'valid_from': timezone.now(),
                    'valid_until': timezone.now() + timedelta(days=30)
                }
            )
            if created:
                self.stdout.write(f'  - Promo code "{promo.code}" created')
        
        self.stdout.write(self.style.SUCCESS('Discount configurations created!'))
