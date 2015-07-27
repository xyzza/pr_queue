# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0004_auto_20150426_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Product name')),
            ],
        ),
        migrations.RemoveField(
            model_name='developerinqueue',
            name='dev',
        ),
        migrations.RemoveField(
            model_name='developerinqueue',
            name='queue',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='queue',
        ),
        migrations.AddField(
            model_name='developer',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DeveloperInQueue',
        ),
        migrations.DeleteModel(
            name='Queue',
        ),
        migrations.AddField(
            model_name='product',
            name='developer',
            field=models.ManyToManyField(to='developers.Developer'),
        ),
    ]
