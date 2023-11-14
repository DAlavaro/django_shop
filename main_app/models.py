from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    descriptions = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='product/', verbose_name='Фотографии', **NULLABLE)
    category = models.CharField(max_length=255, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    date = models.DateField(verbose_name='Дата создания')
    last_date = models.DateField(verbose_name='Дата изменения')

    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Category(models.Model):
    pass