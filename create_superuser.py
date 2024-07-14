import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alumni.alumni.settings")
django.setup()

User = get_user_model()

User.objects.create_superuser(email="student@yandex.ru", password="admin", first_name="Ivan", last_name="Pupkin")