# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperInQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('can_review', models.BooleanField(verbose_name='Can he watch PRs')),
                ('can_be_assigned', models.BooleanField(verbose_name='Is he can do review him self')),
                ('dev', models.ForeignKey(to='developers.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('days', models.CharField(max_length=7, verbose_name='days when queue active')),
                ('active', models.BooleanField(verbose_name='is queue active?')),
            ],
        ),
        migrations.AddField(
            model_name='developerinqueue',
            name='queue',
            field=models.ForeignKey(to='developers.Queue'),
        ),
        migrations.AddField(
            model_name='developer',
            name='queue',
            field=models.ManyToManyField(to='developers.Queue', through='developers.DeveloperInQueue'),
        ),
    ]
