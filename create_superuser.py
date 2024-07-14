from django.contrib.auth import get_user_model

User = get_user_model()

User.objects.create_superuser(email="student@yandex.ru", password="admin", first_name="Ivan", last_name="Pupkin")