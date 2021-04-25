from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.forms.category_create_form import CategoryCreateForm


@login_required
def category_create_view(request):
    form = CategoryCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'BAŞARILI --> Yeni Ürün Kategorisi Oluşturuldu.')
        return redirect('products:product-list')
    context = {
        "form": form,
        "title": "Yeni Ürün Kategorisi Ekle",
    }
    return render(request, "products/product-create.html", context)