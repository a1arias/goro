# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import articles.models


class Migration(migrations.Migration):

    def forward(apps, schema_editor):
        Article = apps.get_model("articles", "Article")
        for a in Article.objects.all():
            a.preview = a.content
            a.save()


    def backward(apps, schema_editor):
        pass

    dependencies = [
        ('articles', '0005_slug_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='preview',
            field=models.TextField(null=True)
        ),
        migrations.RunPython(
            forward,
            backward
        ),
        migrations.AlterField(
            model_name='article',
            name='preview',
            field=models.TextField(null=False)
        ),
    ]
