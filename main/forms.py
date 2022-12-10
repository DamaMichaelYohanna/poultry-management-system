from django import forms

from main.models import Store


class RestockForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"