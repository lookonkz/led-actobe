# Generated by Django 2.0.3 on 2018-03-13 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('phone', models.CharField(max_length=50, verbose_name='телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['date'],
            },
        ),
    ]
