# Generated by Django 2.0.3 on 2018-03-13 07:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20180313_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='price'),
        ),
    ]
