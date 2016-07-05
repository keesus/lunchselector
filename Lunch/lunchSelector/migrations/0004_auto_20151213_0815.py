# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lunchSelector', '0003_auto_20151213_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='o_menu',
        ),
        migrations.AddField(
            model_name='order',
            name='o_menu_text',
            field=models.CharField(default=datetime.datetime(2015, 12, 13, 8, 15, 4, 647723, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
