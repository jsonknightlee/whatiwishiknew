# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0044_auto_20160905_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default='static/placeholder.jpg', upload_to=''),
        ),
    ]
