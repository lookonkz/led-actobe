# Generated by Django 2.0.3 on 2018-03-14 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180314_0452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='produc',
            new_name='product',
        ),
    ]
