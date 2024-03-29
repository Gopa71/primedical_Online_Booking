# Generated by Django 5.0.2 on 2024-02-18 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('banner', models.ImageField(upload_to='bnr')),
                ('photo', models.ImageField(upload_to='pic')),
                ('available', models.BooleanField(default=True)),
                ('desc', models.TextField(blank=True)),
                ('title_1', models.TextField(max_length=250)),
                ('title_2', models.TextField(max_length=250)),
                ('title_3', models.TextField(max_length=250)),
                ('title_4', models.TextField(max_length=250)),
                ('desc_1', models.TextField(blank=True)),
                ('desc_2', models.TextField(blank=True)),
                ('desc_3', models.TextField(blank=True)),
                ('desc_4', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('banner', models.ImageField(upload_to='br')),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('banner', models.ImageField(upload_to='bar')),
                ('photo', models.ImageField(upload_to='pic')),
                ('available', models.BooleanField(default=True)),
                ('desc', models.TextField(blank=True)),
                ('title_1', models.TextField(max_length=250)),
                ('title_2', models.TextField(max_length=250)),
                ('title_3', models.TextField(max_length=250)),
                ('title_4', models.TextField(max_length=250)),
                ('desc_1', models.TextField(blank=True)),
                ('desc_2', models.TextField(blank=True)),
                ('desc_3', models.TextField(blank=True)),
                ('desc_4', models.TextField(blank=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicepp.service')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
    ]
