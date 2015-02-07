from django import forms
from line.models import Item

class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
                'text': forms.fields.TextInput(attrs={
                    'placeholder': 'Enter a line',
                    }),
        }

    def save(self):
        return super().save()