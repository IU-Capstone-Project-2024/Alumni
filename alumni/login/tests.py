from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import CustomUser

User = get_user_model()

class UserLoginTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'test@example.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid email or password')
