from django.shortcuts import render, get_object_or_404
from .models import *


page_defaults = {
    'title': 'basşlıksız ',
    'body': ''
}


def homepage(request):
    news = News.objects.filter(category=music_category)


    return render(request,'pages/index.html', {
        'news': news,
        'music_category':music_category,


    })



def about(request):
    content = {
        'title': 'Hakkında',
        'body':'<h1>Hakkında asdf</h1>'
    }

    context = {
        **page_defaults,
        **content
    }
    return render(request, 'pages/about.html', context)


def contact(request):
    content = {
        'title': 'İletişim',
        'body':'<h1>İletişim asdf</h1>'
    }

    context = {
        **page_defaults,
        **content
    }
    return render(request, 'pages/contact.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'pages/news_detail.html', {
        'news': news,
    })







