# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-28 00:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_auto_20180527_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwishlist',
            name='user',
        ),
        migrations.AddField(
            model_name='userwishlist',
            name='user',
            field=models.ForeignKey(default=-99, on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='wishlist.User'),
            preserve_default=False,
        ),
    ]
