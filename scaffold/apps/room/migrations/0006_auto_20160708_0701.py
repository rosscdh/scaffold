# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_remove_product_rooms'),
        ('room', '0005_roompackage_room_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roompackage',
            name='stock_records',
        ),
        migrations.AddField(
            model_name='roompackage',
            name='products',
            field=models.ManyToManyField(to='catalogue.Product', blank=True),
        ),
    ]
