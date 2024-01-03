from django.db import models
from pytils.translit import slugify
from django.urls import reverse


NULLABLE = {'blank': True, 'null': True}


class Reviews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Nickname')
    content = models.TextField(verbose_name='Отзыв', **NULLABLE)
    photo = models.ImageField(upload_to='reviews/', verbose_name='Изображение', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, auto_created=True, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def get_absolute_url(self):
        return reverse('reviews_app:view', kwargs={'slug': self.slug})
