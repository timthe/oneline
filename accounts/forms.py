from django import forms
from accounts.models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture', 'comment')

#password reset 하는 메일 보내는 것과 관련된 링크
#http://stackoverflow.com/questions/18928144/django-user-registration-password-reset-via-email