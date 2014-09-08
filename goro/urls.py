from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',

    # Examples:
    #url(r'^$', 'goro.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('articles.urls'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^articles/', include('articles.urls', namespace='articles'), name='articles'),
)
