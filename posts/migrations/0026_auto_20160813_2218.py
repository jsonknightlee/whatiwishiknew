# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_auto_20160813_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='posts.Categories'),
        ),
    ]
