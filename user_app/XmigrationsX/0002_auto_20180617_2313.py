# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-17 23:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='portfollio',
            new_name='portfolio',
        ),
    ]