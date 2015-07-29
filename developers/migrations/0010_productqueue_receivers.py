# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0009_auto_20150727_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='productqueue',
            name='receivers',
            field=models.ManyToManyField(to='developers.Developer'),
        ),
    ]
