from django import forms
from products.models.product_model import Category


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if not name:
    #         raise forms.ValidationError('Yeni bir kategori ismi girmeniz gerekiyor')