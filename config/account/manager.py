import os
import sys
from django.core.management import execute_from_command_line
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    try:

        import django
        django.setup()

        create_superuser()

        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


def create_superuser():
    User = get_user_model()
    email = 'admin@example.com'
    username = 'admin'
    password = 'adminpassword'

    if not User.objects.filter(email=email).exists():
        User.objects.create_superuser(email=email, username=username, password=password)
        print(f'Superuser created with email: {email}, username: {username}')
    else:
        print(f'Superuser with email: {email} already exists.')




    if __name__ == '__main__':
        main()