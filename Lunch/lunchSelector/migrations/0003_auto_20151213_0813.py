# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunchSelector', '0002_auto_20151213_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'date_published')),
                ('o_menu', models.ForeignKey(to='lunchSelector.Menu')),
            ],
        ),
        migrations.DeleteModel(
            name='DayInfo',
        ),
    ]
