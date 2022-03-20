# ==========================================01.02.2022
# СУБД - система управления базами данных
# SQL- язык структурированных запросов
# SQlite -
# Primary key (PK) - первичный ключ:
# -суррогатный(искуственный)
# - логический ключ


# import sqlite3 as sq
#
# with sq.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute('DROP TABLE users')
# cur.execute("""
# CREATE TABLE IF NOT EXISTS users(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# summa REAL,
# data TEXT
# )
# """)


# =====================================================03.03.2022

# import sqlite3 as sq

# with sq.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     INSERT INTO person
#     VALUES (10, 'Ольга', '79879755627', 25, 'test@mail.ru')
#     """)
#     # cur.execute("""
#     # CREATE TABLE IF NOT EXISTS person(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # phone BLOB NOT NULL DEFAULT +79879750000,
#     # age  INTEGER NOT NULL CHECK(age > 0 AND age <100),
#     # email TEXT UNIQUE
#     # )
#     # """)
# =================================

# with sq.connect('db_4.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5;
#     """)
#
#     res = cur.fetchone()
#     print(res)
#     res2 = cur.fetchmany(3)
#     print(res2)
#
#     # for res in cur:
#     #     print(res)
#
#     # res = cur.fetchall()
#     # print(res)
# ==============================================15.03.2022
# import sqlite3 as sq

# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
# cur.execute('UPDATE cars SET price = :Price WHERE model LIKE "B%"', {'Price': 0})
# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

# for car in cars:
#     cur.execute('INSERT INTO cars VALUES(NULL, ?, ?)', car)
# ===================================
# import sqlite3 as sq


# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]

# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#
#     """)
#     con.commit()
#
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print('Ошибка выполнения запроса')
# finally:
#     if con:
#         con.close()
# ========================
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#         CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#         );
#         CREATE TABLE IF NOT EXISTS cost(
#             name TEXT, tr_in INTEGER, buy INTEGER
#         );
#         """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_row_id = cur.lastrowid
#     buy_cars_id = 3
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_cars_id))

# ====================


# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     """)
#
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     # rows = cur.fetchmany(5)
#     # print(rows)
#
#     for res in cur:
#         print(res['model'], res['price'])
# =============================
# import sqlite3 as sq
#
# def read_ava(n):
#     try:
#         with open(f'Avatars/{n}.png', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#         );
#         """)
#     cur.execute('SELECT ava FROM users LIMIT 1')
#     img = cur.fetchone()['ava']
#
#     write_ava('out.png', img)


# img = read_ava(1)
# if img:
#     binary = sq.Binary(img)
#     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))


# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     with open('sql_dump.sql', 'r') as f:
#         sql = f.read()
#         cur.executescript(sql)


# with open('sql_dump.sql', 'w') as f:
#     for sql in con.iterdump():
#         f.write(sql)

# for sql in con.iterdump():
#     print(sql)

# =========================================================

# import sqlite3 as sq
#
# data = [('car', 'машина'), ('house', 'дом'), ('tree', 'дерево'), ('color', 'цвет')]
#
# con = sq.connect(":memory:")
# with con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     rus TEXT
#     )
#     """)
#     cur.executemany('INSERT INTO dict VALUES(?, ?)', data)
#
#     cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
#     print(cur.fetchall())

#=====================================================================


