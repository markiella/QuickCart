from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Product

class Command(BaseCommand):
    help = 'Fix missing or empty slugs for existing products'

    def handle(self, *args, **options):
        products_without_slugs = Product.objects.filter(slug__isnull=True) | Product.objects.filter(slug='')
        
        fixed_count = 0
        for product in products_without_slugs:
            slug = slugify(product.name)
            counter = 1
            original_slug = slug
            
            # Ensure unique slug
            while Product.objects.filter(slug=slug).exclude(id=product.id).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            
            product.slug = slug
            product.save()
            fixed_count += 1
            
            self.stdout.write(
                self.style.SUCCESS(f'Fixed slug for product: {product.name} -> {slug}')
            )
        
        if fixed_count == 0:
            self.stdout.write(
                self.style.SUCCESS('All products already have valid slugs!')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully fixed {fixed_count} product slugs!')
            )
