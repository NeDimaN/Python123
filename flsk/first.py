import sqlite3
import os

from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from UserLogin import UserLogin
from admin.admin import admin

# конфигурация
DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'a57489912b7806ba3f3db26e79d623fe3f367851'
MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)


app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))
app.register_blueprint(admin, url_prefix='/admin')

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Авторизуйтесь для доступа к закрытым страницам'
login_manager.login_message_category = 'success'


# menu = [{'name': 'Главная', 'url': 'index'},
#         {'name': 'О нас', 'url': 'about'},
#         {'name': 'Обратная связь', 'url': 'contact'}]

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
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


dbase = None


@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.route('/')
# @app.route('/index')
def index():
    return render_template('index.html', title='Главная', menu=dbase.get_menu(), posts=dbase.get_post_anonce())


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')

    return render_template('add_post.html', title='Добавление статьи', menu=dbase.get_menu())


@app.route('/post/<alias>')
@login_required
def show_post(alias):
    title, post = dbase.get_post(alias)
    if not title:
        abort(404)
    return render_template('post.html', title=title, post=post, menu=dbase.get_menu())


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        user = dbase.get_user_by_email(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            user_login = UserLogin().create(user)
            login_user(user_login)
            return redirect(request.args.get('next') or url_for('profile'))
        flash('Неверная пара логин/пароль', category='error')

    return render_template('login.html', menu=dbase.get_menu(), title='Авторизация')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 and len(request.form['psw']) > 4 and \
                request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.add_user(request.form['name'], request.form['email'], hash)
            if res:
                flash('Вы успешно зарегестрированы', category='success')
                return redirect(url_for('login'))
            else:
                flash('Ошибка при добавлении в базу данных', category='error')

    return render_template('register.html', menu=dbase.get_menu(), title='Регистрация')


@login_manager.user_loader
def load_user(user_id):
    print('load_user')
    return UserLogin().from_db(user_id, dbase)


@app.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('profile.html', menu=dbase.get_menu(), title='Профиль')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта', category='success')
    return redirect(url_for('login'))


@app.route('/userava')
@login_required
def userava():
    img = current_user.get_avatar(app)
    if not img:
        return ''
    h = app.make_response(img)
    h.headers['Content-Type'] = 'image/png'
    return h


@app.route('/upload', methods=['POST', 'GET'])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and current_user.verify_ext(file.filename):
            try:
                img = file.read()
                res = dbase.update_user_avatar(img, current_user.get_id())
                if not res:
                    flash('Ошибка обновления аватара', category='error')
                flash('Аватар обновлен', category='success')
            except FileNotFoundError as e:
                flash('Ошибка обновления аватара', category='error')
        else:
            flash('Ошибка обновления аватара', category='error')
    return redirect(url_for('profile'))


# @app.route('/about')
# def about():
#     return render_template('about.html', title='О нас', menu=[])
#
#
# @app.route('/contact', methods=["POST", "GET"])
# def contact():
#     if request.method == 'POST':
#         if len(request.form['username']) > 2:
#             flash('Сообщение отправлено успешно!', category='success')
#         else:
#             flash('Ошибка отправки!', category='error')
#         # print(request.form)
#         # context = {
#         #     'username': request.form['username'],
#         #     'email': request.form['email'],
#         #     'message': request.form['message']
#         # }
#         # return render_template('contact.html', **context, title='Обратная связь', menu=menu)
#     return render_template('contact.html', title='Обратная связь', menu=[])
#
#
# @app.route('/profile/<path:username>')
# def profile(username):
#     if 'userLogged' not in session or session['userLogged'] != username:
#         abort(401)
#     return f"Пользователь: {username}"
#
#
# # with app.test_request_context():
# #     print(url_for('index'))
# #     print(url_for('about'))
# #     print(url_for('profile', username='ndn'))
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if 'userLogged' in session:
#         return redirect(url_for('profile', username=session['userLogged']))
#     elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['passw'] == '12345':
#         session['userLogged'] = request.form['username']
#         return redirect(url_for('profile', username=session['userLogged']))
#     return render_template('login.html', title='Авторизация', menu=[])
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page404.html', title='Страница не найдена!', menu=[])


if __name__ == '__main__':
    app.run(debug=True)
