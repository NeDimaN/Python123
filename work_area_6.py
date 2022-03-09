#==========================================01.02.2022
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



#=====================================================03.03.2022

import sqlite3 as sq

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
#=================================

with sq.connect('db_4.db') as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2, 5;
    """)

    res = cur.fetchone()
    print(res)
    res2 = cur.fetchmany(3)
    print(res2)

    # for res in cur:
    #     print(res)

    # res = cur.fetchall()
    # print(res)
