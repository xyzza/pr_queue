# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0006_developer__on_duty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='_on_duty',
            new_name='on_duty',
        ),
    ]
