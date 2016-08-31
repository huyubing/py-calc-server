#!/usr/bin/python

import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute('''CREATE TABLE category
        (id int primary key, sort int, name text)''')

c.execute('''CREATE TABLE book
        (id int primary key,
         sort int,
         name text,
         price real,
         category int,
         FOREIGN KEY(category) REFERENCES category(id))''')

conn.commit()

conn.close()
