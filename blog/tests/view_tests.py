from django.test import TestCase

from avirdigital import settings


class BlogTest(TestCase):
    def test_index(self):
        response = self.client.get(f'/{settings.LANGUAGE_CODE}/blog/')
        self.assertEqual(response.status_code, 200)

    def test_view(self):
        response = self.client.get(f'/{settings.LANGUAGE_CODE}/blog/view/{1}')
        self.assertEqual(response.status_code, 200)
