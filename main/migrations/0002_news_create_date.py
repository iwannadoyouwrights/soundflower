# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-23 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='create_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
