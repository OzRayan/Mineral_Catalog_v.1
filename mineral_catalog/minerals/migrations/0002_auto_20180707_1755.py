# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-07-07 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='category',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='cleavage',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='color',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_habit',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_symmetry',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_system',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='diaphaneity',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='formula',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='group',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='image_caption',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='image_filename',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='luster',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='mohs_scale_hardness',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='optical_properties',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='refractive_index',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='specific_gravity',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='streak',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='strunz_classification',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='unit_cell',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
