from django.contrib import admin
from .models import *


class ActiveAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)}
    list_display = ('id', 'title', 'photo', 'time_created', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)}
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    # list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_created')


admin.site.register(Active, ActiveAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
