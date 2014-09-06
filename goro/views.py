from django.shortcuts import render

def index(request):
    return render(request, 'goro/index.html', {
        'title': 'Hello!',
    })
