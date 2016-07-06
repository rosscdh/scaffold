# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20160304_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_type', models.CharField(default=b'std_room', max_length=64, choices=[(b'std_room', 'Standard Room'), (b'bedroom', 'Bedroom'), (b'kitchen', 'Kitchen'), (b'toilet', 'Toilet'), (b'bathroom', 'Bathroom'), (b'sauna', 'Sauna'), (b'jacuzzi', 'Jacuzzi')])),
                ('description', models.CharField(max_length=255)),
                ('data', jsonfield.fields.JSONField(default={})),
                ('product', models.ForeignKey(to='catalogue.Product')),
            ],
        ),
    ]
