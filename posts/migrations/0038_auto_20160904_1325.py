# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0037_auto_20160904_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to=''),
        ),
    ]