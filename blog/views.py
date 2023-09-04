from django.shortcuts import render, get_object_or_404
from .models import *


page_defaults = {
    'title': 'basşlıksız ',
    'body': ''
}


def homepage(request):
    yazilar = Yazi.objects.all()
    return render(request,'pages/index.html', {
        'yazilar': yazilar
    })

# def blog_detail(request, slug):
#     yazi = get_object_or_404(Yazi, slug=slug)

#     return render(request,'pages/blog_detail.html', {
#         'yazi':yazi
#     })




    # name = 'Berker'
    # content = {
    #     'title': 'Anasayfa',
    #     'body':'<h1>Anasayfa asdf</h1>'
    # }

    # context = {
    #     **page_defaults,
    #     **content
    # }

    # return render(request, 'pages/index.html', context)


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


def MusicNews1(request):
    return render(request, 'pages/MusicNews1.html')

def newslist(request):
    news = News.objects.all() 
    return render(request, 'pages/newslist.html', {'news': news})

def blog_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'pages/blog_detail.html', {'news_item': news_item})


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'pages/news_detail.html', {
        'news': news,
    })
