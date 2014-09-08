from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from articles.models import Article
from articles.utils import unslugify

def index(request):

    articles = Article.objects.all()[:5]
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def year_archive(request, year):
    articles = get_list_or_404(Article, pub_date__year=year)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/year_archive.html', context)

def detail(request, slug):
    """
    Slug can be 'something-like-this'
    TODO: add support for 'something like this' <-- note the spaces
    """
    s = unslugify(slug)
    #article = get_object_or_404(Article, headline__contains=s)
    articles = Article.objects.filter(
            headline__contains=s).order_by('pub_date')
    if(articles.count() == 1):
        context = {
            'article': articles[0]
        }
        template = 'articles/detail.html'
    else:
        context = {
            'articles': articles
        }
        template = 'articles/index.html'

    return render(request, template, context)
