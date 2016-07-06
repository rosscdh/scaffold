# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
        ('catalogue', '0008_auto_20160304_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='data',
            field=jsonfield.fields.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='product',
            name='rooms',
            field=models.ManyToManyField(related_name='product_rooms', to='room.Room'),
        ),
    ]
