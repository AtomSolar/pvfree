# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-11-25 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0005_auto_20181124_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvmodule',
            name='Notes',
            field=models.TextField(max_length=100),
        ),
    ]