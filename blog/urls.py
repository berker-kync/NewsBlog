from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name = 'Homepage'),
   path('about/', views.about, name = 'About'), 
   path('contact/', views.contact, name = 'Contact'),
   path('post/<slug>/', views.blog_detail, name ='blog_detail'),
   path('ana/', views.ana, name = 'Ana'), 
   path('MusicNews1.html', views.MusicNews1, name='MusicNews1'),
   path('newslist.html/', views.newslist, name='newslist'),
   path('music_category/<slug>/', views.music_category, name='music_category'),
]
