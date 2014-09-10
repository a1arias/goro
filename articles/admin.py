from django.contrib import admin
from . import models

class ArticleModelAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(models.Article)
admin.site.register(models.Reporter)
admin.site.register(models.Series)
