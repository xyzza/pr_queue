# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0005_auto_20150426_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='_on_duty',
            field=models.BooleanField(default=False, verbose_name='Developer is busy', editable=False),
        ),
    ]
