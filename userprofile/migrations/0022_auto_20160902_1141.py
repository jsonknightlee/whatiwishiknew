# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0021_auto_20160902_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(default='static/placeholder.jpg', null=True, upload_to=''),
        ),
    ]
