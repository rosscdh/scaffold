# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='short_description',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
