from django.db import models
from django.utils.text import slugify

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Series(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'series'

class Article(models.Model):
    def __str__(self):
        return self.headline

    pub_date = models.DateField()
    slug = models.SlugField(max_length=200, unique=True)
    headline = models.CharField(max_length=200)
    preview = models.TextField(null=False)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter)
    series = models.ForeignKey(Series,
                               blank=True,
                               null=True,
                               on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline);
        super(Article, self).save(*args, **kwargs)
