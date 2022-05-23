from django.contrib import admin
from .models import *


class MainAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)}
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Main, MainAdmin)
