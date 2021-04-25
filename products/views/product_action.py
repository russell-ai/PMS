from django.contrib import messages
from django.shortcuts import render, redirect
from products.forms.product_action_form import ProductActionForm
from products.models.action_model import Actions
from products.models.product_model import Product
from django.contrib.auth.decorators import login_required


def product_action_view(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductActionForm(instance=product)
    # TODO: Bu alan sadece ürüne yönelik işlem için ileride tekrar düzenlenecek
    context = {
        'form': form,
        'title': 'Stok Güncelle',
        'pk': pk
    }
    return render(request, 'products/product-action.html', context)
