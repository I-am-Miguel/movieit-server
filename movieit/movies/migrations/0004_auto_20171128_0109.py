# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20171127_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='ratings',
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb_rating',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='metascore',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='rotten_rating',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
