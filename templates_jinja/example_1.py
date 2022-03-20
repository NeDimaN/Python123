from jinja2 import Template

# name = 'Игорь'
# age = 28

# per = {'name': 'Игорь', 'age': 28}
#
# # tm = Template('Привет {{ p.name }}. Мне {{ p.age}} лет.')
# tm = Template('Привет {{ p["name"] }}. Мне {{ p["age"]}} лет.')
# msg = tm.render(p=per)
#
# print(msg)
# {{ }}- выражение для вставки конструкции Python в шаблон
# {% %}- спецификатор шаблона
# {# #}- блок коментариев
# ##- строковый коментарий

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person('Игорь', 28)
# tm = Template('Привет {{ p.get_name() }}. Мне {{ p.get_age()}} лет.')
# msg = tm.render(p=per)
#
# print(msg)

# ==============================================================

# data = """Модуль Jinja вместо определения {{ name }}
# подставит соответствующее значение
# """
#
# tm = Template(data)
# msg = tm.render(name='Игорь')
# print(msg)
# ===========================================
# {%raw%}...{%endraw%}

# data = """{%raw%}Модуль Jinja вместо определения {{ name }}
# подставит соответствующее значение{%endraw%}
# """
#
# tm = Template(data)
# msg = tm.render(name='Игорь')
# print(msg)

# ==========================================


# link = "<a href='#'>Ссылка</a>"
# tm = Template('{{link | e}}')
# msg = tm.render(link=link)
#
# print(msg)
# {{name | e}}- экранирование
# {% for <выражение> %}
#    <повторяющийся фрагмент>
# {% endfor %}
# ==============================
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Житомир'},
#     {'id': 5, 'city': 'Ярославль'}
# ]
#
# link = """<select name='cities'>
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value={{ c['id']}}>{{ c['city']}}</option>
# {% elif c.city == 'Москва'-%}
#     <option>{{ c['city']}}</option>
# {% else -%}
#     {{c['city']}}
# {% endif -%}
# {% endfor -%}
# </select>
#
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)


# {% if <условие>%}
# <фрагмент при истинности условия>
# {% endif %}
# =======================================================

# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'}
#
# ]
#
# link = """<ul>
#
#
# </ul>
# """
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)

# ============================================

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 21000},
    {'model': 'Renault', 'price': 18000},
    {'model': 'BMW', 'price': 44000}
]

lst = [1, 2, 3, 4, 5, 6]

tpl = "Максимальная  цена автомобилей {{ cs | replace('model', 'brand') }}"

tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)
