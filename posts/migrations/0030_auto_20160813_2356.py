# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0029_auto_20160813_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hats', to='posts.Categories'),
        ),
    ]
