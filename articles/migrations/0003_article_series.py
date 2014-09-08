# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, to='articles.Series'),
            preserve_default=True,
        ),
    ]
