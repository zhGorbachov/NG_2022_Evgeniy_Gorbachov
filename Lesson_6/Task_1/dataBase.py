import sqlite3
from sqlite3 import Error


def createConnection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connected")
    except Error as e:
        print(e)
        print("Connection failed!")
    return conn


def createDataBase(connection):
    sql = "CREATE TABLE IF NOT EXISTS users( id integer PRIMARY KEY, nickname text NOT NULL, message text NOT NULL);"
    connection.execute(sql)


def prepareDataBase(name):
    conn = createConnection(name)
    createDataBase(conn)
    conn.close()


def getNicknamesAndMessageFromDB(name):
    connection = createConnection(name)
    sql = "SELECT nickname, message FROM users;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    return rows


def printNicknamesAndMessages(rows):
    text = ""
    for row in rows:
        text += "<h3>"
        for words in row:
            text += "<fieldset>" + str(words) + "<br>"
        text += "</h3>" + "</fieldset>" + "<br>"
    return text


def enterNicknamesAndMessagesInDB(db, nickname, message):
    connection = createConnection(db)
    sql = "INSERT INTO users(`nickname`, `message`) VALUES('{}', '{}')".format(nickname, message)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()
