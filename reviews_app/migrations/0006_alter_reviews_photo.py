# Generated by Django 4.2.7 on 2024-01-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0005_rename_view_count_reviews_views_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='photo',
            field=models.ImageField(blank=True, default='/media/reviews/nobody.png', null=True, upload_to='reviews/', verbose_name='Изображение'),
        ),
    ]