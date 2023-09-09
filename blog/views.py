from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CommentForm
from django.views.generic.edit import CreateView



page_defaults = {
    'title': 'başlıksız ',
    'body': ''
}


def homepage(request):
    categories = Category.objects.all()
    news = News.objects.all()

    latest_music = News.objects.filter(category = '1').order_by('-created_on')[:6]
    latest_technology = News.objects.filter(category = '3').order_by('-created_on')[:6]
    latest_gaming = News.objects.filter(category = '4').order_by('-created_on')[:8]
    latest_anime = News.objects.filter(category = '2').order_by('-created_on')[:6]
    latest_magazine = News.objects.filter(category = '5').order_by('-created_on')[:3]


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
        'latest_magazine': latest_magazine,   
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
    comments = Comment.objects.filter(news=news).order_by('-created')[:5]
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news_detail', slug=slug)
    else:
        form = CommentForm()  # Create a new CommentForm instance for GET requests

    categories = Category.objects.all()
    return render(request, 'pages/news_detail.html', {'news': news, 'categories': categories, 'comments': comments, 'form': form})





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

def magazine(request):
    categories = Category.objects.get(category='Magazine')
    news = News.objects.filter(category=categories)

    return render(request, 'pages/magazine.html', {
        'news': news,
        'categories': categories
    })



class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'pages/add_comment.html'
    # fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(category='Magazine')
        news = News.objects.filter(category__in=categories)
        context['news'] = news
        context['categories'] = categories
        return context


