# Generated by Django 5.1.3 on 2024-11-25 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_cart_owner_cart_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='owner',
        ),
    ]