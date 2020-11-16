from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ConvertViewTests(APITestCase):
    """
    Ensure that conver view works as expected.
    """

    def test_one_hundred(self):

        url = reverse('ntos:convert', kwargs={'number': 100})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('num_in_english'), 'one hundo')
