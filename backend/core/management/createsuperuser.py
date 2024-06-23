from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from django.utils import timezone
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create a Comuna instance
        comuna = Comuna.objects.create(name='san bernardo')

        # Pass the id of the Comuna instance to createsuperuser
        CustomUser.objects.createsuperuser('admin', 'admin@admin.com', 'password', id_comuna=comuna.id)


from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from core.models import CustomUser, Comuna

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create a Comuna instance
        comuna = Comuna.objects.create(name='san bernardo')

        # Check if the Comuna instance was created successfully
        if comuna.id is not None:
            print(f'Comuna instance was created successfully with id {comuna.id}')

            # Pass the id of the Comuna instance to createsuperuser
            CustomUser.createsuperuser('admin', 'admin@myproject.com', 'password', id_comuna=comuna.id)
        else:
            print('Failed to create Comuna instance')

class Command(createsuperuser.Command):
    help = 'Create a superuser, and allow date of birth to be set'

    def handle(self, *args, **options):
        options['interactive'] = options.get('interactive', True)
        database = options.get('database')
        password = None

        if not options.get('username'):
            input_msg = 'Username: '
            username = input(input_msg).strip()
        else:
            username = options.get('username')

        if not options.get('email'):
            input_msg = 'Email address: '
            email = input(input_msg).strip()
        else:
            email = options.get('email')

        if options.get('interactive'):
            fecha_nacimiento_str = input('Date of birth (yyyy-mm-dd): ').strip()
            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()
        else:
            fecha_nacimiento = timezone.now().date()

        extra_fields = {
            'user_type': '3',  # replace with your default value
            'nombre': 'default_name',  # replace with your default value
            'ap_paterno': 'default_value',  # replace with your default value
            'ap_materno': 'default_value',  # replace with your default value
            'telefono': 'default_value',  # replace with your default value
            'direccion': 'default_value',  # replace with your default value
            'fecha_creacion': timezone.now(),  # replace with your default value
            'ultimo_acceso': timezone.now(),  # replace with your default value
            'id_comuna': 'default_value',  # replace with your default value
        }

        CustomUser.objects.create_superuser(username=username, email=email, fecha_nacimiento=fecha_nacimiento, password=password, **extra_fields)