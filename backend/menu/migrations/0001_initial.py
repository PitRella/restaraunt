# Generated by Django 5.1.7 on 2025-03-13 06:58

import menu.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProvisionMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Меню')),
            ],
        ),
        migrations.CreateModel(
            name='Provision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва страви')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=menu.utils.provision_image_path, verbose_name='Зображення страви')),
                ('description', models.TextField(max_length=500, verbose_name='Опис страви')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('calories', models.PositiveSmallIntegerField(verbose_name='Калорії')),
                ('grams', models.PositiveSmallIntegerField(verbose_name='Вага страви')),
                ('menus', models.ManyToManyField(related_name='dishes', to='menu.provisionmenu', verbose_name='Меню страви')),
            ],
        ),
    ]
