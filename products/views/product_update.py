from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.forms.product_update_form import ProductUpdateForm
from products.models.product_model import Product


@login_required
def product_update_view(request, pk):
    queryset = Product.objects.get(id=pk)
    form = ProductUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            quantity = form.cleaned_data['quantity']
            form.save()
            messages.success(request, f"BAŞARILI -->{product_name} Ürün {quantity} birim olarak güncellendi.")
            return redirect('products:product-list')

    context = {
        'form': form,
        'title': 'Stok Güncelle',
        'pk': pk
    }
    return render(request, 'products/product-update.html', context)
