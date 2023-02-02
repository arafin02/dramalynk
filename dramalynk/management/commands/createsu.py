from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='arafin02',
                email='arafin02@oytlook.com',
                password='ILovePromi#65'
            )
        print('Superuser has been created.')
