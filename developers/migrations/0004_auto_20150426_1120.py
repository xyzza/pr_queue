# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0003_queue_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developerinqueue',
            name='can_be_assigned',
        ),
        migrations.AddField(
            model_name='developerinqueue',
            name='can_send_pr',
            field=models.BooleanField(default=True, verbose_name='Can send pull requests'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='queue',
            name='active',
            field=models.BooleanField(default=False, verbose_name='is queue active?'),
        ),
    ]
