# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0007_auto_20150426_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='developer',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='product',
            name='_current',
            field=models.SmallIntegerField(default=0, verbose_name=b'current developers index', editable=False),
        ),
        migrations.AlterField(
            model_name='developer',
            name='on_duty',
            field=models.BooleanField(default=False, verbose_name='Developer can be chosen to reviewers', editable=False),
        ),
    ]
