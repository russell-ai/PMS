from django import forms

from products.models.action_model import Actions


class ActionCreateForm(forms.ModelForm):
    class Meta:
        model = Actions
        fields = ['action_type', 'product_name', 'action_quantity', 'customer']