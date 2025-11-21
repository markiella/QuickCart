"""
Management command to generate product images based on product names.
Uses Pexels API (free, no authentication required) to fetch real product images.
Usage: python manage.py generate_product_images
"""

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from store.models import Product
import requests
from io import BytesIO
from PIL import Image
import time


class Command(BaseCommand):
    help = 'Generate product images from Pexels API based on product names'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force regenerate images even if they already exist',
        )

    def handle(self, *args, **options):
        force = options.get('force', False)
        
        # Get all products without images or with force flag
        if force:
            products = Product.objects.all()
            self.stdout.write(self.style.WARNING('Force regenerating all product images...'))
        else:
            products = Product.objects.filter(image__isnull=True)
            self.stdout.write(self.style.SUCCESS(f'Found {products.count()} products without images'))
        
        if not products.exists():
            self.stdout.write(self.style.SUCCESS('All products already have images!'))
            return
        
        success_count = 0
        error_count = 0
        
        for product in products:
            try:
                self.stdout.write(f'Generating image for: {product.name}...', ending=' ')
                
                # Fetch image from Pexels
                image_data = self.fetch_image_from_pexels(product.name)
                
                if image_data:
                    # Save image to product
                    filename = f'{product.slug}.jpg'
                    product.image.save(filename, ContentFile(image_data), save=True)
                    self.stdout.write(self.style.SUCCESS('✓ Done'))
                    success_count += 1
                else:
                    self.stdout.write(self.style.ERROR('✗ Failed to fetch image'))
                    error_count += 1
                
                # Rate limiting
                time.sleep(0.5)
                    
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error: {str(e)}'))
                error_count += 1
        
        # Summary
        self.stdout.write('\n' + '='*50)
        self.stdout.write(self.style.SUCCESS(f'Successfully generated: {success_count} images'))
        if error_count > 0:
            self.stdout.write(self.style.ERROR(f'Failed: {error_count} images'))
        self.stdout.write('='*50)

    def fetch_image_from_pexels(self, product_name):
        """
        Fetch image from Pexels API based on product name.
        Pexels is free and doesn't require authentication for basic usage.
        Returns image bytes or None if failed.
        """
        try:
            # Pexels API endpoint (free, no auth required)
            url = 'https://api.pexels.com/v1/search'
            
            headers = {
                'Authorization': 'aBYjpXg2EAYccvzZaNv6ACTXmJYDmQ0sq4uV70E2QkByMVvW8puALKkb'  # Get free key from pexels.com/api
            }
            
            params = {
                'query': product_name,
                'per_page': 1,
                'orientation': 'square'
            }
            
            # Make request to Pexels API
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('photos'):
                # Get the first result
                photo = data['photos'][0]
                image_url = photo['src']['medium']
                
                # Download the image
                img_response = requests.get(image_url, timeout=10)
                img_response.raise_for_status()
                
                # Optimize image
                img = Image.open(BytesIO(img_response.content))
                
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'LA', 'P'):
                    rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = rgb_img
                
                # Resize to standard size (500x500)
                img.thumbnail((500, 500), Image.Resampling.LANCZOS)
                
                # Save to bytes
                img_bytes = BytesIO()
                img.save(img_bytes, format='JPEG', quality=85)
                img_bytes.seek(0)
                
                return img_bytes.getvalue()
            
            return None
            
        except requests.exceptions.RequestException as e:
            print(f'Request error: {e}')
            return None
        except Exception as e:
            print(f'Error processing image: {e}')
            return None
