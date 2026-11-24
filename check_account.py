import sqlite3
import bcrypt

def check_account(username, password):
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users_tbl WHERE username = ?", (username,))
    username1 = cursor.fetchone()
    if not username1:
        connection.close()
        return False
    if bcrypt.checkpw(hashed_password=username1[3], password=password.encode()):
        connection.close()
        return True
    connection.close()
    return False
