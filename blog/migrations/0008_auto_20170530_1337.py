# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-30 04:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170528_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tagmodel',
            old_name='Title',
            new_name='title',
        ),
    ]