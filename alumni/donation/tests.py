from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class DonationPageTests(TestCase):
    def test_donation_page_status_code(self):
        response = self.client.get(reverse('donation'))
        self.assertEqual(response.status_code, 200)

    def test_donation_page_template_used(self):
        response = self.client.get(reverse('donation'))
        self.assertTemplateUsed(response, 'donation/donation.html')

    def test_donation_form_submission(self):
        form_data = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'j.doe@innopolis.university',
            'telegram': '@johnDoe',
            'description': 'Description.'
        }
        response = self.client.post(reverse('donation'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you for your donation!')
