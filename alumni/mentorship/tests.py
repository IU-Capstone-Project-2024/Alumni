from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class MentorshipTests(TestCase):


    def test_mentorship_welcome_page_status_code(self):
        response = self.client.get(reverse('intro'))
        self.assertEqual(response.status_code, 200)

    def test_mentorship_welcome_page_content(self):
        response = self.client.get(reverse('intro'))
        self.assertContains(response, 'MENTORSHIP')
        self.assertContains(response, 'Mentorship is a great opportunity for you to help students and guide them through the tough aspects of university life.')
        self.assertContains(response, 'BECOME A MENTOR')

    def test_mentorship_form_page_status_code(self):
        response = self.client.get(reverse('form'))
        self.assertEqual(response.status_code, 200)

    def test_mentorship_form_page_content(self):
        response = self.client.get(reverse('form'))
        self.assertContains(response, 'Please, introduce yourself for the better match with your future mentees.')
        self.assertContains(response, 'About you')
        self.assertContains(response, 'When you are available')
        self.assertContains(response, 'Your motivation')
        self.assertContains(response, 'Telegram alias')
        self.assertContains(response, 'Individual mentorship')
        self.assertContains(response, 'Group mentorship')
        self.assertContains(response, 'SUBMIT')

    def test_mentorship_form_submission(self):
        form_data = {
            'about-you': 'Hi, I am Anna...',
            'availability': 'I am free to take 2 people for once a week meetings...',
            'motivation': 'I want to be a mentor because...',
            'telegram-alias': '@example',
            'mentorship-type': ['individual-mentorship', 'group-mentorship']
        }
        response = self.client.post(reverse('form'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('thank_you'))

    def test_thank_you_page_status_code(self):
        response = self.client.get(reverse('thank_you'))
        self.assertEqual(response.status_code, 200)

    def test_thank_you_page_content(self):
        response = self.client.get(reverse('thank_you'))
        self.assertContains(response, 'Thank you for joining our mentorship program')
        self.assertContains(response, 'We will reach out to you soon.')
        self.assertContains(response, 'BACK TO MENTORSHIP PAGE')
