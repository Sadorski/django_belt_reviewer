# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-23 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beltreviewer', '0002_book_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.TextField(),
        ),
    ]
