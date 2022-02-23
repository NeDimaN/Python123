from bs4 import BeautifulSoup
import requests
import re


class Parser:
    html = ''

    def __init__(self, url):
        self.url = url

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        elements = self.html.find_all('div', class_='model-price-range')  # список []
        prices = []
        for element in elements:
            pr1 = element.find_all('span')[0].text
            price1 = re.sub(r'\D', '', pr1)
            pr2 = element.find_all('span')[1].text
            price2 = re.sub(r'\D', '', pr2)
            if price2.isnumeric():
                prices.append((int(price1) + int(price2)) / 2)
            else:
                prices.append(int(price1))

        return sum(prices) / len(prices)

    def run(self):
        self.get_html()
        return self.parsing()


av = []
for i in range(15):
    pars = Parser(f'https://www.e-katalog.ru/list/206/{i}/')
    av.append(pars.run())
print(av)
print(f'Средняя цена: {round(sum(av) / len(av), 2)} руб.')
