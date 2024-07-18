from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from login.models import CustomUser
from django.conf import settings
import os

class UserProfileTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='password123',
            first_name='Test',
            last_name='User',
            graduation_year=2025,
            position='Developer',
            company='TestCompany',
            location='TestCity',
            interests='Coding',
            activities='Developing apps'
        )
        self.client.login(username='test@example.com', password='password123')

    def test_profile_page_status_code(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_page_displays_user_info(self):
        response = self.client.get(reverse('profile'))
        self.assertContains(response, 'Test User')
        self.assertContains(response, 'Developer')
        self.assertContains(response, 'TestCompany')
        self.assertContains(response, 'TestCity')
        self.assertContains(response, 'Coding')
        self.assertContains(response, 'Developing apps')

    def test_edit_profile(self):
        new_position = 'Senior Developer'
        new_company = 'NewCompany'
        new_location = 'NewCity'
        new_interests = 'Reading'
        new_activities = 'Researching'

        # Create a test image
        test_image = SimpleUploadedFile(
            name='user_photo.png',
            content=open(os.path.join(settings.BASE_DIR, 'media', 'profile_pics', 'user_photo.png'), 'rb').read(),
            content_type='image/png'
        )

        response = self.client.post(reverse('edit_profile'), {
            'user_photo': test_image,
            'graduation_year': 2023,
            'position': new_position,
            'company': new_company,
            'location': new_location,
            'interests': new_interests,
            'activities': new_activities
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))

        # Refresh user data from the database
        self.user.refresh_from_db()

        self.assertEqual(self.user.position, new_position)
        self.assertEqual(self.user.company, new_company)
        self.assertEqual(self.user.location, new_location)
        self.assertEqual(self.user.interests, new_interests)
        self.assertEqual(self.user.activities, new_activities)
        self.assertEqual(self.user.graduation_year, 2023)
        self.assertTrue(self.user.user_photo.name.endswith('.png'))