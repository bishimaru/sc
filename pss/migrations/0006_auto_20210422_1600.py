# Generated by Django 2.0.6 on 2021-04-22 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pss', '0005_auto_20210422_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 16, 0, 56, 340253), verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='data',
            name='memo',
            field=models.CharField(max_length=50, null=True, verbose_name='メモ'),
        ),
    ]
