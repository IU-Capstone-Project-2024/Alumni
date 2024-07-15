import os
import django
from alumni.login.models import CustomUser

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alumni.alumni.settings')
django.setup()

superuser = CustomUser.objects.create_superuser(email="student@yandex.ru",
                                                first_name="Oleg",
                                                last_name="Milashkin",
                                                password="admin")
superuser.save()
