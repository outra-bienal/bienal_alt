# Generated by Django 2.0.6 on 2018-07-21 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0017_auto_20180721_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyzedimage',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='actions.Action'),
        ),
    ]
