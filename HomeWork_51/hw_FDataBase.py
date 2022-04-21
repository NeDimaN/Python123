import sqlite3
import time
import math
import re
from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM mainmenu'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из базы данных')
        return []

    def add_product(self, title, text, price, url):
        try:
            self.__cur.execute('SELECT COUNT() as "count" FROM products WHERE url LIKE ?', (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Товар с таким url уже существует')
                return False
            base = url_for('static', filename='images')
            text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>", r"\g<tag>" + base +
                          r"/\g<url>>", text)
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO products VALUES(NULL, ?, ?, ?, ?, ?)', (title, text, price, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления товара в базу данных' + str(e))
            return False
        return True

    def get_product(self, alias):
        try:
            self.__cur.execute(f'SELECT title, text, price FROM products WHERE url LIKE "{alias}" LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                return res

        except sqlite3.Error as e:
            print('Ошибка добавления продукта в базу данных' + str(e))

        return False, False

    def get_post_anonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, text, price, url FROM products ORDER BY time DESC')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка добавления продукта в базу данных' + str(e))

        return []
