from django.db import models
from autoslug import AutoSlugField

class Yazi(models.Model):
    baslik = models.CharField(max_length=120)
    ozet = models.TextField(max_length=300)
    icerik = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True) #bu auto now add tarihin oluşturulduğunda eklenmesini sağlar
    guncellenme_tarihi = models.DateTimeField(auto_now=True) #bu auto now güncellendiğinde tarihin de güncellenmesini sağlar
    slug = AutoSlugField(populate_from='baslik', unique=True, editable=True, blank=True) #editable admin panelinden değiştirilmesini engeller
    class Meta:
        db_table = 'yazilar' #veri kaybetme riskimiz yok db nin içi boşken bu ismi veriyoruz değişiklikleri yapıyoruz
        verbose_name_plural = 'Yazilar'
    def __str__(self):
        return self.baslik
    


class Category(models.Model):
    category = models.CharField(max_length=75, unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.category
    


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, blank=True)
    textbody1 = models.TextField(null=True, blank=True)
    photo1 = models.URLField(null=True, blank=True)
    subtitle = models.CharField(max_length=200)
    textbody2 = models.TextField(null=True, blank=True)
    photo2 = models.URLField(null=True, blank=True)
    textbody3 = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    
    
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name

    
    



     

