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

