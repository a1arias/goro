from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from articles.models import Article
from articles.utils import unslugify

def index(request):
    articles = Article.objects.all().order_by('-pub_date')[:10]
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def year_archive(request, year):
    #articles = get_list_or_404(Article, pub_date__year=year)
    articles = Article.objects.filter(pub_date__year=year)
    context = {
        'articles': articles,
        'year': year
    }
    return render(request, 'articles/year_archive.html', context)

def month_archive(request, year, month):
    articles = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {
        'articles': articles,
        'year': year,
        'month': month
    }
    return render(request, 'articles/month_archive.html', context)

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
