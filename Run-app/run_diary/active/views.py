from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

menu = [
    {'title': 'Упражнения', 'url_name': 'index'},
    {'title': 'Новости', 'url_name': 'index'},
    {'title': 'Активность', 'url_name': 'race'},
    {'title': 'Добавить активность', 'url_name': 'add_page'},
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
        context['cat_selected'] = 0
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Active.objects.filter(is_published=True).select_related('cat')


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


class ActiveCategory(ListView):
    model = Active
    template_name = 'active/race.html'
    context_object_name = 'parts'
    allow_empty = False

    def get_queryset(self):
        return Active.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['parts'][0].cat)
        context['cat_selected'] = context['parts'][0].cat_id
        context['menu'] = menu
        return context


class AddPage(CreateView):
    form_class = AddPartForm
    template_name = 'active/addpage.html'
    success_url = reverse_lazy('race')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление активности'
        context['menu'] = menu
        return context
