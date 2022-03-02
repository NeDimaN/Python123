#==========================================01.02.2022
# СУБД - система управления базами данных
# SQL- язык структурированных запросов
# SQlite -
# Primary key (PK) - первичный ключ:
# -суррогатный(искуственный)
# - логический ключ





import sqlite3 as sq

with sq.connect('profile.db') as con:
    cur = con.cursor()
    cur.execute('DROP TABLE users')
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS users(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # summa REAL,
    # data TEXT
    # )
    # """)



