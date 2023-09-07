from django.contrib import admin
from .models import Yazi, News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'category']
    list_filter = ['category']
    list_display_links = ['title']

    class Meta:
        model = News


admin.site.register(Yazi)
admin.site.register(News, NewsAdmin)
admin.site.register(Category)
