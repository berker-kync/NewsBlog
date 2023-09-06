from django.shortcuts import render, get_object_or_404
from .models import *


page_defaults = {
    'title': 'basşlıksız ',
    'body': ''
}


def homepage(request):
    categories = Category.objects.all()
    news = News.objects.all()

    return render(request, "pages/index.html", {
        "categories": categories, 
        "news": news
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



def music(request):
    categories = Category.objects.get(category='Music')
    news = News.objects.filter(category=categories)

    return render(request, 'pages/music.html', {
        'news': news,
        'categories': categories
    })




