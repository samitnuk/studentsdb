# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='Група'),
        ),
    ]
