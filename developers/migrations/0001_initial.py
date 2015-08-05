# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name="dev's name")),
                ('email', models.EmailField(max_length=150, verbose_name="dev's email")),
                ('is_active', models.BooleanField(verbose_name='Is active')),
                ('on_duty', models.BooleanField(default=False, verbose_name='Developer can be chosen to reviewers', editable=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DevelopersQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_current', models.SmallIntegerField(default=0, verbose_name='current developers index', editable=False)),
                ('name', models.CharField(max_length=100, verbose_name='DevelopersQueue name')),
                ('developer', models.ManyToManyField(to='developers.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Product queue')),
                ('dev_queue', models.ManyToManyField(to='developers.DevelopersQueue')),
                ('receivers', models.ManyToManyField(to='developers.Developer')),
            ],
        ),
    ]
