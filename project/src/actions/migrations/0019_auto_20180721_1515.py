# Generated by Django 2.0.6 on 2018-07-21 18:15

import datetime
from django.db import migrations, models
import yamlfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0018_auto_20180721_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzedimage',
            name='author',
            field=models.CharField(default='', max_length=100, verbose_name='Autor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analyzedimage',
            name='date',
            field=models.DateField(default=datetime.date(2018, 7, 21), verbose_name='Data'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analyzedimage',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analyzedimage',
            name='info',
            field=yamlfield.fields.YAMLField(default='', verbose_name='Resultados da Análise'),
        ),
    ]
