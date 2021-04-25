from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=55, verbose_name='Ürün İsmi', unique=True)
    quantity = models.PositiveIntegerField(verbose_name='Ürün Miktarı')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(verbose_name="Ürün Açıklaması", max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ("-id",)

    def __str__(self):
        return self.product_name


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Kategori İsmi')

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        ordering = ['id']

    def __str__(self):
        return self.name
