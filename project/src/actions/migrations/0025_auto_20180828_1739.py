# Generated by Django 2.0.6 on 2018-08-28 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0024_remove_action_action_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontag',
            name='description_en',
            field=models.TextField(default='', verbose_name='Descrição (EN)'),
        ),
        migrations.AddField(
            model_name='questiontag',
            name='title_en',
            field=models.CharField(default='', max_length=100, verbose_name='Pergunta (EN)'),
        ),
        migrations.AlterField(
            model_name='analyzedimage',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='actions.Action', verbose_name='Ação'),
        ),
        migrations.AlterField(
            model_name='questiontag',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Pergunta'),
        ),
    ]
