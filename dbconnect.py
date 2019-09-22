import sqlite3

def connection():
    conn = sqlite3.connect("user.db")

    c = conn.cursor()

    return c, conn
