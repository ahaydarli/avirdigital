from django.test import TestCase

from avirdigital import settings


class BlogTest(TestCase):
    def test_index(self):
        self.assertEqual(200, 200)
