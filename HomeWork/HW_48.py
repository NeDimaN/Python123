from jinja2 import Template


menu = [
    {'href': '/index', 'link': 'Главная'},
    {'href': '/news', 'link': 'Новости'},
    {'href': '/about', 'link': 'О компании'},
    {'href': '/shop', 'link': 'Магазин'},
    {'href': '/contacts', 'link': 'Контакты'}

]

link = """<ul>
{% for m in menu -%}
{% if m.href ==  '/index' -%}
    <li><a href='{{ m['href'] }}' class="active">{{ m['link'] }}</a></li>
{% else -%}
   <li><a href='{{ m['href'] }}'>{{ m['link'] }}</a></li>
{% endif -%}
{% endfor -%}
</ul>
"""

tm = Template(link)
msg = tm.render(menu=menu)

print(msg)