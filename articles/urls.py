from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'articles.views.index', name='index'),
    url(r'^(?P<year>\d{4})/$', 'articles.views.year_archive', name='year_view'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'articles.views.month_archive', name='month_view'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', 'articles.views.detail', name='detail'),
]
