# Generated by Django 2.0.3 on 2018-03-09 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Главное фото'),
        ),
    ]
