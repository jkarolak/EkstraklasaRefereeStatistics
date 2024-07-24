# Generated by Django 5.0.7 on 2024-07-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referee_stats', '0004_event_type_of_referee_alter_event_referee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type_of_decision',
            field=models.CharField(choices=[('1', 'GOOD_PENALTY'), ('2', 'BAD_PENALTY'), ('3', 'MISS_PENALTY'), ('4', 'GOOD_RED_CARD'), ('5', 'BAD_RED_CARD'), ('6', 'MISS_RED_CARD'), ('7', 'OFFSIDE_GOAL'), ('8', 'ONSIDE_GOAL'), ('9', 'OTHER')], max_length=50, verbose_name='Decyzja'),
        ),
        migrations.AlterField(
            model_name='event',
            name='type_of_referee',
            field=models.CharField(choices=[('1', 'GŁÓWNY'), ('2', 'ASYSTENT 1'), ('3', 'ASYSTENT 2'), ('4', 'TECHNICZNY'), ('5', 'VAR'), ('6', 'VAR ASYSTENT')], max_length=50, verbose_name='Rola sędziego'),
        ),
    ]
