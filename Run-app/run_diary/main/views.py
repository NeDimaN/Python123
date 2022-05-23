from django.shortcuts import render
from django.views.generic import ListView
from .models import *


menu = [
    {'title': 'Упражнения', 'url_name': 'index'},
    {'title': 'Новости', 'url_name': 'index'},
    {'title': 'Активность', 'url_name': 'race'},
    {'title': 'Блог', 'url_name': 'index'},
    {'title': 'Вход', 'url_name': 'index'},
    {'title': 'Регистрация', 'url_name': 'index'},


]


class MainHome(ListView):
    model = Main
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context


# class ActiveHome(ListView):
#     model = Active
#     template_name = 'main/race.html'
#     context_object_name = 'parts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Активность'
#         context['menu'] = menu
#         return context

