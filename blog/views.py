from django.shortcuts import render, get_object_or_404
from .models import *


page_defaults = {
    'title': 'başlıksız ',
    'body': ''
}


def homepage(request):
    categories = Category.objects.all()
    news = News.objects.all()

    latest_music = News.objects.filter(category = '1').order_by('-created_on')[:6]
    latest_technology = News.objects.filter(category = '2').order_by('-created_on')[:6]
    latest_gaming = News.objects.filter(category = '3').order_by('-created_on')[:8]
    latest_anime = News.objects.filter(category = '4').order_by('-created_on')[:9]


    latest_news_by_category = []

    for category in categories:
        latest_news = News.objects.filter(category=category).order_by('-created_on').first()
        if latest_news:
            latest_news_by_category.append(latest_news)


    return render(request, "pages/index.html", {
        "categories": categories, 
        "news": news,
        'latest_news_by_category': latest_news_by_category,
        'latest_music': latest_music,
        'latest_anime': latest_anime,
        'latest_gaming': latest_gaming,
        'latest_technology': latest_technology,        
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

def gaming(request):
    categories = Category.objects.get(category='Gaming')
    news = News.objects.filter(category=categories)

    return render(request, 'pages/gaming.html', {
        'news': news,
        'categories': categories
    })

def anime(request):
    categories = Category.objects.get(category='Anime')
    news = News.objects.filter(category=categories)

    return render(request, 'pages/anime.html', {
        'news': news,
        'categories': categories
    })

def technology(request):
    categories = Category.objects.get(category='Technology')
    news = News.objects.filter(category=categories)

    return render(request, 'pages/technology.html', {
        'news': news,
        'categories': categories
    })




