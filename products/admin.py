from django.contrib import admin
from products.models.action_model import Actions
from products.models.product_model import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "quantity", "category")
    list_filter = ("product_name", "category")
    fields = (("product_name", "quantity"), ("category", "content"))
    search_fields = ('product_name','category__name')
    list_per_page = 15

class ActionsAdmin(admin.ModelAdmin):
    readonly_fields = ["action_date"]
    list_display = ('action_type','product_name', 'action_quantity', 'action_date')
    list_filter = ("action_type", "product_name")
    fields = ("action_type", "product_name", "action_quantity", "customer", "action_date")
    search_fields = ('action_type', 'product__product_name', 'category__name')
    list_per_page = 15

admin.site.register(Product, ProductAdmin)
admin.site.register(Actions, ActionsAdmin)
admin.site.register(Category)



admin.site.site_header = "STOK YÖNETİM PANELİ"
admin.site.site_title = "Stok Yönetimi"
admin.site.index_title = "Stok Yönetimi"
