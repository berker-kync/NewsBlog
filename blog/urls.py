from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .models import News 
from .views import CommentCreateView


urlpatterns = [
   path('', views.homepage, name = 'Homepage'),
   path('about/', views.about, name = 'About'), 
   path('contact/', views.contact, name = 'Contact'),
   path('news/<slug>/', views.news_detail, name='news_detail'),
   path('music/', views.music, name='Music'),
   path('anime/', views.anime, name='Anime'),
   path('gaming/', views.gaming, name='Gaming'),
   path('technology/', views.technology, name='Technology'),
   path('magazine/', views.magazine, name='Magazine'),
   path('news/<slug:news_slug>/comment/', views.CommentCreateView.as_view(), name='comment_create')
,
]
