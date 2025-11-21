# Quick Cart - Local Grocery Delivery Platform

Quick Cart is a comprehensive Django web application for local grocery and convenience store ordering with free delivery, suki discounts, and first-time customer promotions.

## 🌟 Features

### Core Features
- **Online Grocery Store** - Browse and order fresh vegetables, fruits, snacks, beverages, and ready-made meals
- **Free Local Delivery** - No delivery fees within the service area
- **Suki Discount System** - Loyalty rewards for repeat customers (5%, 10%, 15% discounts)
- **First-Time Customer Promos** - Special discounts for new customers
- **Real-time Stock Management** - Live inventory tracking and updates
- **Order Tracking** - Complete order lifecycle from placement to delivery
- **Responsive Design** - Mobile-friendly interface with modern UI

### User Roles
- **Admin** - Full system management, analytics, user management
- **Staff/Rider** - Order management, delivery updates, inventory management
- **Customer** - Shopping, order placement, order tracking, profile management

### Technical Features
- **Django 5.x** - Modern Python web framework
- **Role-based Access Control** - Secure user management system
- **Bootstrap 5** - Responsive UI framework
- **SQLite/PostgreSQL** - Flexible database support
- **Session-based Cart** - Works for both authenticated and anonymous users
- **AJAX Integration** - Smooth user experience with dynamic updates

## 🎨 Design & Branding

The application uses a vibrant color palette inspired by fresh groceries:
- **Orange (#F15A24)** - Primary brand color, energy and freshness
- **Green (#1EA55B)** - Success states, fresh vegetables
- **Blue (#1A4DB6)** - Information, trust and reliability

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd quickcart
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   # Copy environment file
   copy .env.example .env
   
   # Edit .env file with your settings
   ```

5. **Database setup**
   ```bash
   # Run migrations
   python manage.py makemigrations
   python manage.py migrate
   
   # Create superuser
   python manage.py createsuperuser
   
   # Seed sample data
   python manage.py seed_data
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 👥 Default Users (After Seeding)

### Admin User
- **Username:** admin
- **Password:** admin123
- **Role:** Admin
- **Access:** Full system management

### Staff User
- **Username:** staff
- **Password:** staff123
- **Role:** Staff/Rider
- **Access:** Order management, inventory updates

### Sample Customers
- **Username:** customer1 / **Password:** customer123 (Suki customer with 5 orders)
- **Username:** customer2 / **Password:** customer123 (First-time customer)

## 📱 Application Structure

```
quickcart/
├── quickcart/          # Main project configuration
├── accounts/           # User authentication and profiles
├── store/             # Product catalog and categories
├── cart/              # Shopping cart functionality
├── orders/            # Order management and tracking
├── discounts/         # Discount and promo system
├── dashboard/         # Admin and staff dashboard
├── templates/         # HTML templates
├── static/           # CSS, JavaScript, images
└── media/            # User uploaded files
```

## 🛍️ Key Functionality

### For Customers
1. **Browse Products** - View products by category, search, and filter
2. **Shopping Cart** - Add/remove items, update quantities
3. **Checkout Process** - Enter delivery details, apply discounts
4. **Order Tracking** - Monitor order status from preparation to delivery
5. **Discount Benefits** - Automatic suki discounts and promo codes

### For Staff/Riders
1. **Order Management** - View assigned orders, update delivery status
2. **Inventory Updates** - Update stock levels for products
3. **Delivery Tracking** - Mark orders as delivered with timestamps

### For Admins
1. **Product Management** - Add/edit products, categories, pricing
2. **Order Oversight** - Monitor all orders, assign staff
3. **User Management** - Manage customer accounts, staff assignments
4. **Analytics Dashboard** - Sales reports, popular products, revenue tracking
5. **Discount Configuration** - Set up promo codes, suki discount tiers

## 💰 Discount System

### Suki Discounts (Loyalty Program)
- **Bronze Suki** - 5% discount (3+ orders)
- **Silver Suki** - 10% discount (5+ orders)  
- **Gold Suki** - 15% discount (10+ orders)

### First-Time Customer Promo
- **Welcome Discount** - 10% off first order (minimum ₱200)
- **Maximum discount** - ₱100

### Promo Codes
- **WELCOME20** - 20% off for new customers (min ₱300)
- **SAVE50** - ₱50 off orders above ₱500
- **WEEKEND15** - 15% weekend special (min ₱250)

## 🔧 Configuration

### Environment Variables (.env)
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### Key Settings
- **Free Delivery** - No delivery charges within service area
- **Session Timeout** - 24 hours for cart persistence
- **Stock Alerts** - Low stock warnings at 5 items or below
- **Order Statuses** - Pending → Confirmed → Preparing → Out for Delivery → Delivered

## 📊 Sample Data

The seed command creates:
- **7 Product Categories** - Vegetables, Fruits, Snacks, Beverages, Meals, Dairy, Pantry
- **25+ Products** - Diverse grocery items with realistic pricing
- **3 User Roles** - Admin, Staff, and Customer accounts
- **Discount Configurations** - Suki tiers, first-time promos, sample promo codes

## 🎯 Business Features

### Local Focus
- **Community-Centered** - Designed for local grocery stores and communities
- **Filipino Market** - Pricing in Philippine Peso (₱), local products
- **Cultural Integration** - "Suki" system reflects Filipino business culture

### Operational Efficiency
- **Real-time Inventory** - Prevents overselling, tracks stock levels
- **Order Workflow** - Streamlined process from order to delivery
- **Staff Assignment** - Efficient delivery management system

## 🔒 Security Features

- **Role-based Access** - Secure user permissions and access control
- **CSRF Protection** - Built-in Django security features
- **Input Validation** - Form validation and data sanitization
- **Session Security** - Secure session management

## 📱 Mobile Responsive

- **Bootstrap 5** - Mobile-first responsive design
- **Touch Friendly** - Optimized for mobile shopping experience
- **Fast Loading** - Optimized images and efficient code

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG=False` in production
2. Configure proper database (PostgreSQL recommended)
3. Set up email backend for notifications
4. Configure static file serving
5. Set up proper domain and SSL certificate

### Recommended Hosting
- **Heroku** - Easy Django deployment
- **DigitalOcean** - VPS with more control
- **PythonAnywhere** - Python-focused hosting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- **Email:** info@quickcart.ph
- **Phone:** +63 123 456 7890
- **Hours:** Daily 6AM - 10PM

## 🙏 Acknowledgments

- Built with Django and Bootstrap
- Inspired by local Filipino grocery stores and suki culture
- Designed for community-focused e-commerce

---

**Quick Cart** - Fresh groceries delivered free to your door! 🛒🚚
