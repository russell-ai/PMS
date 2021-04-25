from django import forms
from products.models.product_model import Product


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'quantity', 'category', 'content']
