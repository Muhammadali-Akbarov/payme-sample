from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GeneratePayLinkAPIViewTestCase(APITestCase):

    def test_generate_pay_link(self):
        url = reverse('generate-pay-link')
        data = {
            'order_id': 999,
            'amount': 999,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('pay_link', response.data)
