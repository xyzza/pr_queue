# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0008_auto_20150727_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Product queue')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='DeveloperQueue name'),
        ),
        migrations.AddField(
            model_name='productqueue',
            name='dev_queue',
            field=models.ManyToManyField(to='developers.Product'),
        ),
    ]
