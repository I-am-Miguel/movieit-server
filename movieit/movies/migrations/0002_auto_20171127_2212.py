# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='content_rating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.MovieGenre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='movie',
            name='posterHorizontal',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='posterPortrait',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.ManyToManyField(to='movies.Rating'),
        ),
        migrations.AddField(
            model_name='movie',
            name='synopsis',
            field=models.CharField(default='', max_length=400),
        ),
    ]