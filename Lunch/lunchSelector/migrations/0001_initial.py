# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'date_published')),
                ('d_count', models.IntegerField(default=0)),
                ('d_menu_text', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_text', models.CharField(max_length=30)),
                ('count', models.IntegerField(default=0)),
                ('count_permanent', models.IntegerField(default=0)),
            ],
        ),
    ]
