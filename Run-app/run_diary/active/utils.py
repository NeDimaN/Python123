
from django.db.models import Count
from .models import *

menu = [
    {'title': 'Упражнения', 'url_name': 'index'},
    {'title': 'Новости', 'url_name': 'news'},
    # {'title': 'Активность', 'url_name': 'race'},
    {'title': 'Добавить активность', 'url_name': 'add_page'},
    {'title': 'Блог', 'url_name': 'index'},


]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('active'))

        context['menu'] = menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
