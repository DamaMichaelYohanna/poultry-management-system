from django import forms
from django.contrib.auth import get_user_model


from account.models import Profile
class UserForm(forms.ModelForm):
    """good with arrows"""

    class Meta:
        get_user_model()
        fields = "__all__"


class ProfileForm(forms.ModelForm):
    """good with arrows"""

    class Meta:
        model = Profile
        fields = "__all__"