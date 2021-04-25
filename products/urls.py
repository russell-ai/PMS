from django.urls import path
from products.views.category_create import category_create_view
from products.views.product_action import product_action_view
from products.views.product_create import product_create_view
from products.views.product_delete import product_delete_view
from products.views.product_detail import product_detail_view
from products.views.product_list import product_list, stock_actions_list_view
from products.views.product_update import product_update_view
from products.views.stock_action import stock_action_view

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product-list'),
    path('update/<int:pk>/', product_update_view, name='product-update'),
    path('product-action/<int:pk>/', product_action_view, name='product-action'),
    path('detail/<int:pk>/', product_detail_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
    path('delete/<int:pk>/', product_delete_view, name='product-delete'),
    path('action/', stock_action_view, name='action-create'),
    path('action/list/', stock_actions_list_view, name='action-list'),
    path('category/create/', category_create_view, name='category-create'),
]
