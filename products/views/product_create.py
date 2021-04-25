from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.forms.product_create_form import ProductCreateForm


@login_required
def product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Stok ekleme başarılı.')
        return redirect('products:product-list')

    context = {
        "form": form,
        "title": "Ürün Ekle",
    }

    return render(request, "products/product-create.html", context)

# class ProductCreateView(CreateView):
#     template_name = "products/product-create.html"
#     form_class = ProductCreateForm
