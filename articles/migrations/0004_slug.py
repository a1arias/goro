# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.text import slugify
import articles.models


def forward(apps, schema_editor):
    Article = apps.get_model("articles", "Article")
    for a in Article.objects.all():
        a.slug = slugify(a.headline)
        a.save(update_fields=['slug'])


def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_series'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'series'},
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.RunPython(
            forward,
            backward
        )
    ]
