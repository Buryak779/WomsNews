from django.contrib import admin
from news.models import News, Category, Tag, Comments
from django_summernote.admin import SummernoteModelAdmin


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_min','text')

admin.site.register(News, NewsAdmin)#Отображение полей в админ странице статьи
admin.site.register(Category)#Отображение полей в админ странице категорий
admin.site.register(Tag)#Отображение полей в админ странице тегов

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')
admin.site.register(Comments,CommentsAdmin)#Отображение комментариев в админ странице