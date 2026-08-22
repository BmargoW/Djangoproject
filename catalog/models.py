from django.db import models


class Category(models.Model):
    title_name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.CharField(max_length=150, verbose_name="Описание")

    def __str__(self):
        return f"{self.title_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title_name"]


class Product(models.Model):
    STATUS_CHOICES = [('published', 'опубликован'), ('not_published', 'не опубликован'), ]

    product_name = models.CharField(max_length=150, verbose_name="Название")
    product_description = models.CharField(max_length=150, verbose_name="Описание")
    picture = models.ImageField(upload_to="catalog/picture", verbose_name="Изображение", blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    purchase_price = models.IntegerField(null=True, verbose_name="Цена за покупку")
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    status_publications = models.CharField(max_length=30, choices=STATUS_CHOICES, default = 'not_published', verbose_name="Публикация")

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name"]
