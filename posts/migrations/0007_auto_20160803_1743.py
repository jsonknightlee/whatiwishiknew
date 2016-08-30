# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 15:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20160803_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cmntr', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
