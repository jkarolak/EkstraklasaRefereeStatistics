# Generated by Django 5.0.7 on 2024-07-23 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referee_stats', '0003_event_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type_of_referee',
            field=models.IntegerField(choices=[('1', 'GŁÓWNY'), ('2', 'ASYSTENT 1'), ('3', 'ASYSTENT 2'), ('4', 'TECHNICZNY'), ('5', 'VAR'), ('6', 'VAR ASYSTENT')], default=1, verbose_name='Rola sędziego'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='referee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='referee', to='referee_stats.referee', verbose_name='Sędzia'),
        ),
    ]
