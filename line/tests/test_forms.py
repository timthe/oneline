from django.test import TestCase
from line.forms import ItemForm
from line.models import Item

class ItemFormTest(TestCase):
    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a line"', form.as_p())