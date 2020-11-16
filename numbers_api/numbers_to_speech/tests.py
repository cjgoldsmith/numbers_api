
from django.urls import reverse
from hypothesis import given
import hypothesis.strategies as st
from hypothesis.extra.django import TestCase as HypothesisTestCase
from rest_framework import status
from rest_framework.test import APITestCase
from numbers_to_speech.views import ConvertView


class ConvertViewTests(APITestCase):
    """
    Ensure that conver view works as expected.
    """

    def test_one_hundred(self):

        url = reverse('ntos:convert', kwargs={'number': 123})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('num_in_english'), 'one hundred twenty three')

    def test_parse_hundred(self):
        self.assertEqual(ConvertView.parse_hundred('023'), 'twenty three')
        self.assertEqual(ConvertView.parse_hundred('005'), 'five')
        self.assertEqual(ConvertView.parse_hundred('955'), 'nine hundred fifty five')

    def test_parse_number(self):
        self.assertEqual(ConvertView.parse_number('1024'), 'one thousand twenty four')
        self.assertEqual(ConvertView.parse_number('2541024'), 'two million five hundred fourty one thousand twenty four')
        self.assertEqual(ConvertView.parse_number('-46'), 'negative fourty six')


class ConvertTests(HypothesisTestCase):

    @given(n=st.integers())
    def test_hypothesis_numbers(self, n):
        ConvertView.parse_number(str(n))

        # This test case is only looking for edge case exceptions.
        self.assertTrue(True)
