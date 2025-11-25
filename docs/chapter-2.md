# CHAPTER II: METHODOLOGY AND SYSTEM DESIGN  

### 2.1 Project Methodology  

The study adopted the **Agile** software development life cycle, which is characterized by iterative and incremental development guided by continuous user feedback. In the planning and requirements gathering phase, the researchers conducted interviews and informal discussions with local store owners, staff, riders, and frequent customers to identify pain points in the existing manual process. These consultations formed the basis for defining both the functional and non-functional requirements of the system.

During the initial analysis and design iteration, the team modeled the system using the Input–Process–Output (IPO) framework, context diagrams, and data flow diagrams. The initial database schema and wireframes for key interfaces—such as the home page, cart, checkout, and dashboards—were also designed in this stage. Development was then carried out incrementally by implementing the Django project and the modular apps (`accounts`, `store`, `cart`, `orders`, `discounts`, `dashboard`, and `notifications`). Features were built in logical increments, starting from authentication and product browsing, followed by cart and checkout flows, discount logic, dashboards, and notification mechanisms.

Testing activities were performed throughout development. Unit and integration tests were created for critical components such as discount calculations, order creation, and role-based views, and internal testing was used to verify that end-to-end flows—for example, from customer checkout to rider delivery—worked as intended. After core functionalities were in place, user acceptance testing and refinement were conducted with representative users using predefined scenarios. Feedback collected through questionnaires and informal interviews led to refinements in the user interface and several processes, including order status labeling and notification behavior. Finally, a functional version of Quick Cart was deployed to a cloud hosting provider (e.g., Render) using Gunicorn and Whitenoise for static file serving. This cyclical Agile approach allowed the researchers to progressively adapt and improve the system based on emerging insights.

### 2.2 Technical System Architecture  

Quick Cart follows a **three-tier, client–server architecture** that separates concerns into presentation, application, and data layers. This structure improves maintainability, scalability, and security by clearly delineating responsibilities across the stack.

At the **presentation layer** on the client side, users interact with the system through a web browser interface built using HTML, CSS, JavaScript, and Bootstrap 5. The layout is responsive so that customers, staff, and riders can use the system on desktops, laptops, tablets, and mobile devices without losing core functionality or readability.

The **application layer** on the server side is implemented using the Django 5 framework running on Python. This layer contains the modular apps that encapsulate specific domains of functionality: `accounts` manages the custom user model, registration, login, and role management; `store` handles products, categories, and product listings; `cart` manages session-based cart operations; `orders` is responsible for order creation, tracking, and status updates; `discounts` manages *suki* tiers, first-time customer promos, and promo codes; `dashboard` aggregates data for admin and staff dashboards; and `notifications` delivers user-specific alerts.

The **data layer** stores and manages the system’s persistent data. By default, the system uses SQLite for development but can be configured to use PostgreSQL in production. Django models represent users, products, orders, discounts, and notifications, while media storage is used to handle product images. HTTP requests from clients are routed to Django views in the application layer, which interact with the database through the ORM and render templates back to the presentation layer. In production, static and media files are served efficiently using Django in conjunction with Whitenoise.

### 2.2.1 System Environment (Hardware and Software Requirements)  

#### Hardware Requirements (Minimum)  

For development, Quick Cart requires a machine with at least a dual‑core 2.0 GHz processor, 8 GB of RAM, and a minimum of 20 GB of free storage, along with a stable internet connection for installing dependencies and accessing external services. For deployment, a small cloud instance is sufficient, typically with 1–2 virtual CPUs, 1–2 GB of RAM, and adequate disk space to store the database and media files such as product images.

#### Software Requirements  

On the server or development environment, the system can run on Windows 10+, macOS, or Linux and requires Python 3.8 or higher together with Django 5.x. Several supporting libraries are necessary: `Pillow` for image handling, `django-crispy-forms` and `crispy-bootstrap5` for form rendering, `python-decouple` for environment variable management, `requests` for integrating with the Pexels API, `Whitenoise` for static file serving, and `gunicorn` as the WSGI server in production deployments. On the client side, any modern web browser such as Google Chrome, Mozilla Firefox, Microsoft Edge, or Safari can be used to access the application.

### 2.3 System Modeling and Blueprints  

#### 2.3.1 System Flowchart / Data Flow Diagrams  

The system can be represented by a context diagram that highlights its main external entities, processes, and data stores. The primary external entities are the Customer, Admin, Staff, and Rider, each of whom interacts with the system in different ways. Customers submit orders and track their status, admins and staff manage products, discounts, and orders, while riders receive assigned deliveries and update order statuses.

At a high level, the main processes include managing products and inventory, processing customer orders, managing discounts and promotional configurations, assigning and delivering orders, and generating notifications about important events. These processes interact with several core data stores: user data, products and categories, orders and order items, discount and promo code configurations, and notifications. A Level 0 Data Flow Diagram (DFD) can be used to show how data moves from customers placing orders through order processing and discount computation to rider assignment and final delivery updates.

*(Insert Figure 2 and Figure 3 here to illustrate the context and data flow diagrams.)*

#### 2.3.2 Wireframes and User Interface Prototypes  

Wireframes were created to define the layout and component placement for the main user interfaces before implementation. For customers, the home page presents featured products, categories, and navigation elements that guide users into the catalog. Product listing and detail pages display product images, descriptions, and actions such as “Add to Cart,” while the shopping cart page summarizes selected items, quantities, prices, and computed subtotals. The checkout page collects delivery information, presents applicable discounts, and shows the final total amount.

For administrators and staff, the dashboard provides an overview of recent orders, low stock alerts, and shortcuts to key management pages. Staff and rider views list assigned orders along with the necessary details to update order statuses as deliveries progress. These wireframes serve as blueprints for the final UI and can be illustrated in figures showing sample layouts and screenshots of the implemented interfaces.

#### 2.3.3 Database Structure and Design  

The database is designed to conform to at least **Third Normal Form (3NF)** in order to minimize redundancy and maintain data integrity. At its core, the schema includes a `User` entity that stores authentication data and attributes such as role, contact information, total orders, and flags related to *suki* eligibility. Product-related data is organized into `Category` and `Product` entities, where categories group products into logical groupings (for example, Fresh Vegetables or Snacks), and product records contain details such as name, description, price, stock quantity, unit, category association, and image reference.

Orders are represented by an `Order` entity that records the customer, delivery address, total amount, applied discounts, assigned staff or rider, and current order status. Individual items within each order are stored in `OrderItem`, which captures the product, quantity, unit price, and subtotal for each line. Discount-related behavior is modeled through `SukiDiscount`, which defines loyalty tiers based on minimum order counts and discount percentages, `FirstTimeCustomerPromo`, which stores configuration for first-order promotions, and `PromoCode`, which defines customizable promo codes with their discount types and conditions. Finally, a `Notification` entity records user-targeted alerts and messages related to orders and other system events. These entities and their relationships are typically represented in an Entity–Relationship Diagram (ERD) and summarized in a table describing each major database table.

### 2.4 Implementation Procedures  

The implementation of Quick Cart followed a series of structured steps. First, the development environment was prepared by installing Python, creating a virtual environment, and installing the required dependencies from `requirements.txt`. Environment variables were configured using a `.env` file based on `.env.example`, including the secret key, debug mode, database URL, and email settings.

Next, the Django project `quickcart` and its supporting apps (`accounts`, `store`, `cart`, `orders`, `discounts`, `dashboard`, and `notifications`) were created and added to `INSTALLED_APPS`. Template directories, static file paths, and media settings were configured to support the front-end and asset management. Models for users, products, orders, discounts, and notifications were then defined, migrations were applied, and the `seed_data` management command was used to populate the database with realistic sample data.

After the data layer was established, the main views, URLs, and templates were implemented. Views were created for product listing, cart operations, checkout, order tracking, and dashboards, and URL patterns were organized within each app and in the project-level router. Responsive templates using Bootstrap and the Django template language were developed to provide a consistent user interface across roles and devices. The system’s discount logic was integrated using the `SukiDiscount`, `FirstTimeCustomerPromo`, and `PromoCode` models, while notification logic was added so that riders and customers receive timely updates about order-related events. The Pexels API was integrated through the `generate_product_images` management command to automatically assign images to products.

Throughout development, unit and integration tests were executed on critical modules, and manual exploratory testing was performed to validate complete user flows. Finally, for deployment, the production environment was configured with Gunicorn as the WSGI server and Whitenoise for static file handling, and the system was deployed to a cloud host where core functionalities were verified under realistic conditions.
