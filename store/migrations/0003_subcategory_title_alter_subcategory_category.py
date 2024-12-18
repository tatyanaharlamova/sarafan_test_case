# Generated by Django 5.1.3 on 2024-11-25 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='title',
            field=models.CharField(blank=True, help_text='Укажите название подкатегории', max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='store.category', verbose_name='Подкатегория'),
        ),
    ]
