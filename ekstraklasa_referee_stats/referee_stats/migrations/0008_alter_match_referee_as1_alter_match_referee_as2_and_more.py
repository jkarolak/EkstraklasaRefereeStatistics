# Generated by Django 5.0.7 on 2024-07-23 21:35

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referee_stats', '0007_alter_match_referee_as1_alter_match_referee_as2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='referee_as1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='referee_as1', to='referee_stats.referee', verbose_name='Sędzia asystent 1'),
        ),
        migrations.AlterField(
            model_name='match',
            name='referee_as2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='referee_as2', to='referee_stats.referee', verbose_name='Sędzia asystent 2'),
        ),
        migrations.AlterField(
            model_name='match',
            name='referee_main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='referee_main', to='referee_stats.referee', verbose_name='Sędzia główny'),
        ),
        migrations.AlterField(
            model_name='match',
            name='referee_tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='referee_tech', to='referee_stats.referee', verbose_name='Sędzia techniczny'),
        ),
        migrations.AlterField(
            model_name='match',
            name='referee_var',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='referee_var', to='referee_stats.referee', verbose_name='Sędzia VAR'),
        ),
        migrations.AlterField(
            model_name='match',
            name='referee_vara',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='referee_vara', to='referee_stats.referee', verbose_name='Sędzia VAR asystent'),
        ),
        migrations.AlterField(
            model_name='match',
            name='round',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(34)], verbose_name='Kolejka'),
        ),
    ]
