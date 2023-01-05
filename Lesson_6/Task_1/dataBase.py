import sqlite3
from sqlite3 import Error


def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connected")
    except Error as e:
        print(e)
        print("Connection failed!")
    return conn


def init_tables(connection):
    sql = "CREATE TABLE IF NOT EXISTS users( id integer PRIMARY KEY, login text NOT NULL, message text NOT NULL);"
    connection.execute(sql)


def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()


def getLoginAndMessage(name):
    connection = init_conn(name)
    sql = "SELECT login, message FROM users;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    return rows


def printMessage(rows):
    text = ""
    for row in rows:
        text += "<h3>"
        for words in row:
            text += "<fieldset>" + str(words) + "<br>"
        text += "</h3>" + "</fieldset>" + "<br>"
    return text


def registerUser(db, login, message):
    connection = init_conn(db)
    sql = "INSERT INTO users(`login`, `message`) VALUES('{}', '{}')".format(login, message)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()
