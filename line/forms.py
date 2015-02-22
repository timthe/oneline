from django import forms
from line.models import Category, Item, Comment

class CategoryForm(forms.models.ModelForm):

    class Meta:
        model = Category
        fields = ('name', )


class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('mtype', 'category', 'title', 'picture', 'text', 'user',)
        widgets = {
                'user': forms.HiddenInput()
        }

    # def save(self):
    #     return super().save()

    def save(self, user):
        self.instance.user = user
        return super().save()

class CommentForm(forms.models.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)

    def save(self, user, item):
        self.instance.user = user
        self.instance.item = item
        return super().save()