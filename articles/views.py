from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from articles.models import Article
from articles.utils import unslugify

def index(request):

    articles = Article.objects.all()[:10]
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
    """
    article = get_object_or_404(Article, slug__exact=slug)
    context = {
        'article': article
    }
    template = 'articles/detail.html'

    return render(request, template, context)
