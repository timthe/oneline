from django.test import TestCase
from line.models import Item

class ItemModelsTest(TestCase):
    def test_string_representation(self):
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')