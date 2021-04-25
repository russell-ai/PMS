from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from products.forms.product_search_form import ProductSearchForm
from products.models.action_model import Actions
from products.models.product_model import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@login_required
def product_list(request):
    queryset = Product.objects.all()
    form = ProductSearchForm(request.POST or None)
    if request.method == 'POST':
        query = form['product_name'].value()
        queryset = queryset.filter(Q(product_name__icontains=query) |
                                   Q(category__name__icontains=query)).distinct()

    paginator = Paginator(queryset, 25)  # Show 25 result per page.

    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        'title': 'Ürünlere ait stok listesi',
        'queryset': queryset,
        'form': form
    }

    return render(request, 'products/product-list.html', context)


@login_required
def stock_actions_list_view(request):

    queryset = Actions.objects.all()
    # form = ProductSearchForm(request.POST or None)
    # if request.method == 'POST':
    #     query = form['product_name'].value()
    #
    #     queryset = queryset.filter(Q(product_name__icontains=query) |
    #                                Q(category__icontains=query)).distinct()

    paginator = Paginator(queryset, 50)  # Show 25 result per page.

    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        'title': 'Stok Hareketleri Listesi',
        'queryset': queryset,
        #'form': form,
    }

    return render(request, 'products/action-list.html', context)
