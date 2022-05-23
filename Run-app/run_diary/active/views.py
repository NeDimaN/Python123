from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

menu = [
    {'title': 'Упражнения', 'url_name': 'index'},
    {'title': 'Новости', 'url_name': 'index'},
    {'title': 'Активность', 'url_name': 'race'},
    {'title': 'Добавить активность', 'url_name': 'race'},
    {'title': 'Блог', 'url_name': 'index'},
    {'title': 'Выйти', 'url_name': 'index'},

]


class ActiveHome(ListView):
    model = Active
    template_name = 'active/race.html'
    context_object_name = 'parts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Активность'
        context['menu'] = menu
        return context


class ShowPart(DetailView):
    model = Active
    template_name = 'active/part.html'
    context_object_name = 'part'
    slug_url_kwarg = 'part_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['part']
        context['menu'] = menu
        return context
