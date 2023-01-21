from django import forms

from main.models import Store, GProduct, GProductCategory


class RestockForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"


class GProductForm(forms.ModelForm):
    class Meta:
        models = GProduct
        fields = "__all__"


class GProductCategoryForm(forms.ModelForm):
    class Meta:
        models = GProductCategory
        fields = "__all__"
