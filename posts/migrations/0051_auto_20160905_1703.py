# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0050_auto_20160905_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='static/placeholder.jpg', null=True, upload_to=''),
        ),
    ]
