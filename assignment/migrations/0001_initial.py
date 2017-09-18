# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedDeveloper',
            fields=[
                ('email', models.EmailField(max_length=150, primary_key=True, serialize=False, verbose_name="dev's email")),
                ('name', models.CharField(max_length=150, verbose_name="dev's name")),
                ('is_active', models.BooleanField(verbose_name='Is active')),
                ('category', models.SmallIntegerField(choices=[(1, 'junior'), (2, 'middle'), (3, 'senior')])),
            ],
            options={
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Project code')),
                ('name', models.CharField(max_length=200, verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='ActiveDeveloper',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('assignment.ordereddeveloper',),
        ),
        migrations.AddField(
            model_name='project',
            name='developers',
            field=models.ManyToManyField(to='assignment.ActiveDeveloper'),
        ),
    ]