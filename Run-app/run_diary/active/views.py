from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


from .models import *
from .forms import *
from .utils import *


# menu = [
#     {'title': 'Упражнения', 'url_name': 'index'},
#     {'title': 'Новости', 'url_name': 'index'},
#     {'title': 'Активность', 'url_name': 'race'},
#     {'title': 'Добавить активность', 'url_name': 'add_page'},
#     {'title': 'Блог', 'url_name': 'index'},
#     {'title': 'Выйти', 'url_name': 'index'},
#
# ]


class ActiveHome(DataMixin, ListView):

    model = Active
    template_name = 'active/race.html'
    context_object_name = 'parts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Активность'
        # context['cat_selected'] = 0
        # context['menu'] = menu
        c_def = self.get_user_context(title='Активность')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):

        return Active.objects.filter(is_published=True).select_related('cat')


class ShowPart(DataMixin, DetailView):
    model = Active
    template_name = 'active/part.html'
    context_object_name = 'part'
    slug_url_kwarg = 'part_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['part']
        # context['menu'] = menu
        c_def = self.get_user_context(title=context['part'])
        return dict(list(context.items()) + list(c_def.items()))


class ActiveCategory(DataMixin, ListView):

    model = Active
    template_name = 'active/race.html'
    context_object_name = 'parts'
    allow_empty = False

    def get_queryset(self):
        return Active.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Категория - ' + str(context['parts'][0].cat)
        # context['cat_selected'] = context['parts'][0].cat_id
        # context['menu'] = menu
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPartForm
    template_name = 'active/addpage.html'

    success_url = reverse_lazy('race')
    login_url = reverse_lazy('race')

    def get_context_data(self, *, object_list=None, **kwargs):

        # context['title'] = 'Добавление активности'
        # context['menu'] = menu
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление активности')
        return dict(list(context.items()) + list(c_def.items()))


class NewsPage(DataMixin, ListView):

    model = News
    template_name = 'active/news.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Новости')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):

        return News.objects.filter(is_published=True)


class ShowNews(DataMixin, DetailView):
    model = News
    template_name = 'active/new.html'
    context_object_name = 'new'
    slug_url_kwarg = 'new_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['part']
        # context['menu'] = menu
        c_def = self.get_user_context(title=context['new'])
        return dict(list(context.items()) + list(c_def.items()))

