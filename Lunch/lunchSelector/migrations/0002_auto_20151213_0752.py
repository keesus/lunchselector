# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunchSelector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayinfo',
            name='date',
            field=models.DateTimeField(verbose_name=b'date_published'),
        ),
    ]
