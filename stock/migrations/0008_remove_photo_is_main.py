# Generated by Django 2.0.3 on 2018-03-13 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20180313_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='is_main',
        ),
    ]
