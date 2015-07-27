# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0002_auto_20150426_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='name',
            field=models.CharField(default='Unnamed', max_length=200, verbose_name='Queue name'),
        ),
    ]
