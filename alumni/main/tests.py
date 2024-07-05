from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class MainPageTests(TestCase):
    def test_main_page_status_code(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_main_page_template_used(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'main/main.html')

    def test_main_page_content(self):
        response = self.client.get(reverse('main'))
        self.assertContains(response, 'Welcome to Alumni website!')
