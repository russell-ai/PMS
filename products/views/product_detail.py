from django.shortcuts import render
from products.models.product_model import Product
from django.contrib.auth.decorators import login_required


@login_required
def product_detail_view(request, pk):
    queryset = Product.objects.get(id=pk)
    title = "Ürün Detayı"

    context = {
        'title': title,
        'queryset': queryset,
    }

    return render(request, 'products/product-detail.html', context)
