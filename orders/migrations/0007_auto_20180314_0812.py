# Generated by Django 2.0.3 on 2018-03-14 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_conatacform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conatacform',
            old_name='tel',
            new_name='telephone',
        ),
    ]
