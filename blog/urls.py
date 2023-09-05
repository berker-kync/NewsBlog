from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name = 'Homepage'),
   path('about/', views.about, name = 'About'), 
   path('contact/', views.contact, name = 'Contact'),
   path('news/<slug>/', views.news_detail, name='news_detail')
]
