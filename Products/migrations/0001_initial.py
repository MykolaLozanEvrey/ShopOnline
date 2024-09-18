# Generated by Django 5.0 on 2023-12-27 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Категорія')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': ' Категорія ',
                'verbose_name_plural': ' Категорії ',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Фото')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=30, verbose_name='Назва товару')),
                ('describe', models.CharField(blank=True, max_length=2000, verbose_name='Характеристики')),
                ('price', models.FloatField(verbose_name='Ціна')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.category', verbose_name='Категорії')),
            ],
            options={
                'verbose_name': ' Продукт ',
                'verbose_name_plural': ' Продукти ',
                'ordering': ['name'],
            },
        ),
    ]