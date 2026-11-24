import sqlite3

connection = sqlite3.connect("accounts.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE users_tbl(id INTEGER PRIMARY KEY, email VARCHAR UNIQUE, username VARCHAR, password VARCHAR)")

connection.close()
