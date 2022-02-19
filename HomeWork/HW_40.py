import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('ski_price.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow((data['name'], data['url'], data['old_price'], data['new_price'], data['sale']))


def correct_url(s):
    return f'https://beactiv.ru{s}'


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('div',
                             class_='product_preview lg-grid-4 md-grid-4 sm-grid-4 xs-grid-6 mc-grid-6 padded-inner')

    for el in elements:
        try:
            name = el.find('a').get('title')
        except ValueError:
            name = ''

        try:
            url = el.find('a').get('href')
            url1 = correct_url(url)

        except ValueError:
            url1 = ""

        try:
            sale = el.find('div', class_='product_preview-status--sale').text
        except ValueError:
            sale = ''
        try:
            new_price = el.find('span', class_='prices-current').text.strip()
        except ValueError:
            new_price = ''
        try:
            old_price = el.find('span', class_='prices-old').text.strip()
        except ValueError:
            old_price = ''

        data = {'name': name,
                'url': url1,
                'old_price': old_price,
                'new_price': new_price,
                'sale': sale
                }
        write_csv(data)


def main():
    url = 'https://beactiv.ru/collection/lyzhi-begovye'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
