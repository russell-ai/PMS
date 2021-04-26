from django.db import models
from django.utils import timezone
from products.models.product_model import Product


class Actions(models.Model):
    ACTION_TYPE = [("giriş", "Giriş"), ("çıkış", "Çıkış")]

    action_type = models.CharField(verbose_name='Stok Hareketi', max_length=10, choices=ACTION_TYPE, null=False,
                                   blank=False)
    product_name = models.ForeignKey(Product, verbose_name="Ürün İsmi", on_delete=models.CASCADE, related_query_name='actions')
    action_quantity = models.PositiveIntegerField(verbose_name='İşlem Miktarı', blank=True, null=True, default=0)
    action_date = models.DateTimeField(verbose_name='Tarih-Saat', default=timezone.now)  # models.DateTimeField(default=timezone.now)
    customer = models.CharField(verbose_name='Müşteri', max_length=100, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, default=1)
    quantity = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='action', verbose_name='Miktar')

    class Meta:
        verbose_name = "Stok Hareketi"
        verbose_name_plural = "Stok Hareketleri"
        ordering = ['-action_date']



    def __str__(self):
        return f"{self.product_name}-->{self.action_type}"
