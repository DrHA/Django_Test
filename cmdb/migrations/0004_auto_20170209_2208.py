# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20170209_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='server_list',
            name='update_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='server_list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.UserInfo'),
        ),
    ]
