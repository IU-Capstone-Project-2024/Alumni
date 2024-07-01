from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from .models import Alumni
from datetime import datetime

# Create your tests here.

class CardRequestTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.alumni = Alumni.objects.create(
            name='John',
            surname='Doe',
            email='john.doe@innopolis.university',
            telegram='@johndoe',
            graduation_year=2020
        )
        self.url = reverse('visit')
        self.submit_url = reverse('handle-form-submission')

    def test_page_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_page_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'card_request/card_request.html')

    def test_handle_form_submission(self):
        data = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'john.doe@innopolis.university',
            'telegram': '@johndoe',
            'visit-date': '2024-07-01'
        }
        response = self.client.post(self.submit_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Success'})

        # Check that an email has been sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Alumni - University Visit Request', mail.outbox[0].subject)
        self.assertIn('john.doe@innopolis.university', mail.outbox[0].body)
