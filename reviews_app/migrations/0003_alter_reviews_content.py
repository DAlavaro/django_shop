# Generated by Django 4.2.7 on 2023-12-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0002_alter_reviews_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Отзыв'),
        ),
    ]
