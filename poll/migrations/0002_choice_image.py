# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-21 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
