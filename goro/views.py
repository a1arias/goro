from django.shortcuts import render
from goro.models import Page

def index(request):

    p = Page.objects.get(name__iexact='home')

    return render(request, 'goro/index.html',
                  {'page': p})
