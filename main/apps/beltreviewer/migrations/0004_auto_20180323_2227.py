# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-23 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beltreviewer', '0003_auto_20180323_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]