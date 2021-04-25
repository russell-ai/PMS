from django import forms
from products.models.product_model import Product


class ProductSearchForm(forms.ModelForm):
    # indir_excel_csv = forms.BooleanField(required=False)

    class Meta:
        model = Product
        fields = ['product_name']