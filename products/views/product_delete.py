from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from products.models.product_model import Product


@login_required
def product_delete_view(request, pk):
    queryset = Product.objects.get(id=pk)

    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'BAŞARILI --> Ürün stoklardan silindi.')
        return redirect('products:product-list')
    return render(request, 'products/product-delete.html', {"queryset": queryset, 'title': 'Stok Sil'})
