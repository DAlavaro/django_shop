from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Reviews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='Nickname')
    content = models.TextField(verbose_name='Отзыв', **NULLABLE)
    photo = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, auto_created=True, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
