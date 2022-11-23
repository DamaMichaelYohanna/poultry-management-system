from django import forms
from django.contrib.auth import get_user_model

from account.models import Profile


class UserForm(forms.ModelForm):
    """good with arrows"""

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    """good with arrows"""

    class Meta:
        model = Profile
        exclude = ("user",)
