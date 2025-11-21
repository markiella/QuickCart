from django.core.management.base import BaseCommand
from accounts.models import User

class Command(BaseCommand):
    help = 'Create a test rider account'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, default='rider1', help='Rider username')
        parser.add_argument('--email', type=str, default='rider1@example.com', help='Rider email')
        parser.add_argument('--password', type=str, default='rider123', help='Rider password')
        parser.add_argument('--first-name', type=str, default='John', help='Rider first name')
        parser.add_argument('--last-name', type=str, default='Rider', help='Rider last name')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
        first_name = options['first_name']
        last_name = options['last_name']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Rider account "{username}" already exists'))
            return

        # Create rider user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role='rider'
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created rider account:'))
        self.stdout.write(f'  Username: {username}')
        self.stdout.write(f'  Email: {email}')
        self.stdout.write(f'  Password: {password}')
        self.stdout.write(f'  Name: {first_name} {last_name}')
        self.stdout.write(f'  Role: Rider')
