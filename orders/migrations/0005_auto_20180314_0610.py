# Generated by Django 2.0.3 on 2018-03-14 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180314_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='stock.Product', verbose_name='Товар'),
            preserve_default=False,
        ),
    ]
