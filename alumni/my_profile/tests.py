from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from login.models import CustomUser, Interest
from django.conf import settings
import os

class UserProfileTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            password='testpassword',
            location='TestLocation'
        )

        self.client.login(email='testuser@example.com', password='testpassword')

    def test_profile_page_status_code(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_page_displays_user_info(self):
        response = self.client.get(reverse('profile'))
        self.assertContains(response, 'Test User')

    def test_edit_profile(self):
        new_position = 'Senior Developer'
        new_company = 'NewCompany'
        new_location = 'NewCity'

        test_image_path = os.path.join(settings.BASE_DIR, 'media', 'profile_pics', 'user_photo.png')
        if not os.path.exists(test_image_path):
            with open(test_image_path, 'wb') as f:
                f.write(b'\x00' * 100)

        with open(test_image_path, 'rb') as image_file:
            test_image = SimpleUploadedFile(
                name='user_photo.png',
                content=image_file.read(),
                content_type='image/png'
            )

        response = self.client.post(reverse('edit_profile'), {
            'user_photo': test_image,
            'graduation_year': 2023,
            'position': new_position,
            'company': new_company,
            'location': new_location,
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))

        
        self.user.refresh_from_db()

        self.assertEqual(self.user.position, new_position)
        self.assertEqual(self.user.company, new_company)
        self.assertEqual(self.user.location, new_location)
        self.assertEqual(self.user.graduation_year, 2023)
        self.assertTrue(self.user.user_photo.name.endswith('.png'))
