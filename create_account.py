import sqlite3
import bcrypt

def create_account(email, username, password):
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users_tbl WHERE email = ?", (email,))
    email1 = cursor.fetchone()
    if email1:
        connection.close()
        return False
    cursor.execute("INSERT INTO users_tbl(email, username, password) VALUES(?, ?, ?)", (email, username, bcrypt.hashpw(password.encode(), bcrypt.gensalt())))

    connection.commit()
    connection.close()
    return True
