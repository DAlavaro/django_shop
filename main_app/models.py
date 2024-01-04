from django.db import models
from django.urls import reverse
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='наименование')
    descriptions = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')
    date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    last_date = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

<<<<<<< HEAD
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
=======
    is_active = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
>>>>>>> main

    def __str__(self):
        return f'{self.name} {self.category}'

    def get_absolute_url(self):
        return reverse('candle', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    descriptions = models.TextField(verbose_name='описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('candles', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'