# Generated by Django 4.2.7 on 2023-12-05 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='описание')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='наименование')),
                ('descriptions', models.TextField(verbose_name='описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена за покупку')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('last_date', models.DateField(auto_now=True, verbose_name='дата последнего изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('view_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
            },
        ),
    ]
