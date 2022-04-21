import sqlite3
import os

from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from hw_FDataBase import FDataBase

DATABASE = '/tmp/hw_flsk.db'
DEBUG = True
SECRET_KEY = 'a57489912b7806ba3f3db26e79d623fe3f367851'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'hw_flsk.db')))

dbase = None


@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('hw_sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
def index():
    return render_template('hw_index.html', title='Каталог товаров', menu=dbase.get_menu(),
                           products=dbase.get_post_anonce())


@app.route('/add_product', methods=['POST', 'GET'])
def add_product():
    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_product(request.form['name'], request.form['post'], request.form['price'],
                                    request.form['url'])
            if not res:
                flash('Ошибка добавления товара', category='error')
            else:
                flash('Товар добавлен успешно', category='success')
        else:
            flash('Ошибка добавления товара', category='error')

    return render_template('add_product.html', title='Добавление товара', menu=dbase.get_menu())


@app.route('/product/<alias>')
def show_product(alias):
    title, product, price = dbase.get_product(alias)
    if not title:
        abort(404)
    return render_template('product.html', title=title, product=product, price= price, menu=dbase.get_menu())

if __name__ == '__main__':
    app.run(debug=True)
