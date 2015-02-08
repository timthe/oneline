from django import forms
from line.models import Item

class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text', 'user',)
        widgets = {
                'text': forms.fields.TextInput(attrs={
                    'placeholder': 'Enter a line',
                    }),
        }

    def save(self):
        return super().save()

    # def save(self, user):
    #     self.instance.user = user
    #     return super().save()