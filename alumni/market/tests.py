from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.conf import settings
from .models import Product
from decimal import Decimal

# Create your tests here.

class MarketTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=Decimal('100.00'),
            image='products/test_image.jpg',
            has_sizes=False
        )

    def test_product_list_view(self):
        url = reverse('product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/market.html')
        self.assertContains(response, self.product.name)

    def test_product_detail_view(self):
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/product_details.html')
        self.assertEqual(response.context['product'], self.product)

    def test_product_buy_view_get(self):
        url = reverse('product_buy', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/product_buy.html')
        self.assertEqual(response.context['product'], self.product)
        self.assertIsNone(response.context.get('selected_size'))

    def test_product_buy_view_post(self):
        url = reverse('product_buy', args=[self.product.id])
        data = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'john.doe@example.com',
            'payment_method': 'Credit Card'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect to checkout
        self.assertEqual(len(mail.outbox), 2)  # Two emails should be sent
        self.assertIn('John Doe purchase', mail.outbox[0].subject)
        self.assertIn('Ordering: Test Product', mail.outbox[1].body)

    def test_checkout_view(self):
        # Simulate session data
        session = self.client.session
        session['product_id'] = self.product.id
        session.save()

        url = reverse('checkout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/gratitude_buy.html')
        self.assertEqual(response.context['price'], self.product.price)