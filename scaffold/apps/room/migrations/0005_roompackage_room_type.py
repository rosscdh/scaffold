# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_roompackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='roompackage',
            name='room_type',
            field=models.CharField(default=b'std_room', max_length=64, choices=[(b'std_room', 'Standard Room'), (b'bedroom', 'Bedroom'), (b'kitchen', 'Kitchen'), (b'toilet', 'Toilet'), (b'bathroom', 'Bathroom'), (b'sauna', 'Sauna'), (b'jacuzzi', 'Jacuzzi')]),
        ),
    ]
