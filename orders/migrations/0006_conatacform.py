# Generated by Django 2.0.3 on 2018-03-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20180314_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConatacForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('tel', models.IntegerField(verbose_name='тел')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
            ],
            options={
                'verbose_name': 'Заявка на консультацию',
                'verbose_name_plural': 'Заявки на консультацию',
                'ordering': ['date'],
            },
        ),
    ]
