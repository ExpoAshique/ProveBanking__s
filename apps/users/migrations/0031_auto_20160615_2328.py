# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20160610_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.FileField(null=True, upload_to=users.models._get_resume_upload_path),
        ),
    ]
