# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20160706_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='feature_image',
            field=versatileimagefield.fields.VersatileImageField(upload_to=b'images/rooms/', null=True, verbose_name=b'Image', blank=True),
        ),
    ]
