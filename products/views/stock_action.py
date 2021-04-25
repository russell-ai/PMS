from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from products.forms.action_create_form import ActionCreateForm
from products.models.action_model import Actions
from products.models.product_model import Product

@login_required
def stock_action_view(request):
    # product = Product.objects.get(id=pk)
    # queryset = Actions.objects.filter(product_name_id=product.product_name__id)
    form = ActionCreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        product = Product.objects.get(product_name=instance.product_name)
        if instance.action_type == 'çıkış':
            if product.quantity >= instance.action_quantity:
                product.quantity -= instance.action_quantity
                messages.success(request,
                                 f"BAŞARILI --> Stok çıkışı yapıldı! {str(instance.action_quantity)} birim {str(instance.product_name)}")
                instance.save()
                product.save()
                return redirect('products:product-detail', product.id)

            else:
                messages.success(request, "BAŞARISIZ Stok çıkışı! --> Stok Miktarlarını dikkate alarak çıkış yapınız!!")
                return redirect('products:product-detail', product.id)

        if instance.action_type == 'giriş':
            product.quantity += instance.action_quantity
            instance.save()
            product.save()
            messages.success(request,f"BAŞARILI Stok girişi --> {str(instance.action_quantity)} birim {str(instance.product_name)}")
            return redirect('products:product-detail', product.id)

    context = {
        "title": 'Stok Hareketi',
        "form": form,
    }
    return render(request, "products/action-create.html", context)
