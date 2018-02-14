from django.contrib import admin
from news.models import News, Category, Tag


admin.site.register(News)#Отображение полей в админ странице статьи
admin.site.register(Category)#Отображение полей в админ странице категорий
admin.site.register(Tag)#Отображение полей в админ странице тегов
