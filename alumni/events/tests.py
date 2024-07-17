from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Events
from login.models import Interest, CustomUser
from django.utils import timezone
import json

# Create your tests here.

class EventsViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(email='testuser@example.com', password='password')
        self.interest = Interest.objects.create(name='Interest')
        self.event1 = Events.objects.create(
            event_name='Event 1',
            author_email='author1@example.com',
            author_name='Author',
            author_surname='One',
            author_alias='author1',
            country='Country 1',
            city='City 1',
            address='Address 1',
            date=timezone.now(),
            description='Description for event 1'
        )
        self.event1.tags.add(self.interest)
        self.event2 = Events.objects.create(
            event_name='Event 2',
            author_email='author2@example.com',
            author_name='Author',
            author_surname='Two',
            author_alias='author2',
            country='Country 2',
            city='City 2',
            address='Address 2',
            date=timezone.now(),
            description='Description for event 2'
        )
        self.event2.tags.add(self.interest)

    def test_page(self):
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertIn('countries', response.context)
        self.assertIn('cities', response.context)
        self.assertIn('tags', response.context)
        self.assertIn('events', response.context)

    def test_filter_events(self):
        response = self.client.get(reverse('filter_events'), {'country': 'Country 1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertEqual(len(response.context['events']), 1)
        self.assertEqual(response.context['events'][0], self.event1)

        response = self.client.get(reverse('filter_events'), {'city': 'City 1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertEqual(len(response.context['events']), 1)
        self.assertEqual(response.context['events'][0], self.event1)

        response = self.client.get(reverse('filter_events'), {'tags': [self.interest.pk]})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertEqual(len(response.context['events']), 2)
        self.assertIn(self.event1, response.context['events'])
        self.assertIn(self.event2, response.context['events'])

    def test_ai_recommendation(self):
        self.client.login(email='testuser@example.com', password='password')
        response = self.client.get(reverse('ai_recommendation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertIn('events', response.context)

    def test_event_detail(self):
        response = self.client.get(reverse('event_detail', args=['event-1']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_detail.html')
        self.assertEqual(response.context['event'], self.event1)

    def test_add_activity_authenticated(self):
        self.client.login(email='testuser@example.com', password='password')
        data = json.dumps({'event_link': '/events/event-1'})
        response = self.client.post(reverse('add_activity'), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_add_activity_unauthenticated(self):
        data = json.dumps({'event_link': '/events/event-1'})
        response = self.client.post(reverse('add_activity'), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], False)
        self.assertEqual(response.json()['error'], 'User is not authenticated.')

    def test_delete_activity_authenticated(self):
        self.client.login(email='testuser@example.com', password='password')
        data = json.dumps({'event_link': '/events/event-1'})
        response = self.client.post(reverse('delete_activity'), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_delete_activity_unauthenticated(self):
        data = json.dumps({'event_link': '/events/event-1'})
        response = self.client.post(reverse('delete_activity'), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], False)
        self.assertEqual(response.json()['error'], 'User is not authenticated.')

    def test_add_delete_activity_invalid_method(self):
        self.client.login(email='testuser@example.com', password='password')
        response = self.client.get(reverse('add_activity'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], False)
        self.assertEqual(response.json()['error'], 'Invalid request method.')

        response = self.client.get(reverse('delete_activity'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], False)
        self.assertEqual(response.json()['error'], 'Invalid request method.')
