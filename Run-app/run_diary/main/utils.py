from .models import *


menu = [
    # {'title': 'Упражнения', 'url_name': 'index'},
    # {'title': 'Новости', 'url_name': 'index'},
    # {'title': 'Активность', 'url_name': 'race'},
    # {'title': 'Блог', 'url_name': 'index'},
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Регистрация', 'url_name': 'register'},

]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs




        context['menu'] = menu

        return context
