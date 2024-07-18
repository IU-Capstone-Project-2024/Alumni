from django.test import TestCase, Client
import json

# Create your tests here.

class ChatViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_chat_view_post(self):
        data = {
            'message': 'Hello!'
        }
        response = self.client.post('/chat/', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()['response'], str)

    def test_chat_view_post_empty_message(self):
        response = self.client.post('/chat/', json.dumps({}), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"response": "No input provided"})

    def test_chat_view_invalid_method(self):
        response = self.client.get('/chat/')

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"response": "Invalid request method"})
