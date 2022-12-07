from django import forms

from main.models import Store


class PickOutForm(forms.ModelForm):
    class Meta:
        model = Store
        exclude = ('rate',)
