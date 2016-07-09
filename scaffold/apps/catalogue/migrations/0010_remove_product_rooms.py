# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_auto_20160706_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rooms',
        ),
    ]
