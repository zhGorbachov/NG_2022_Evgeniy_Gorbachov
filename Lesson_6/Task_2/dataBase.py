import sqlite3


def createDataBase(connection):
    sql = "CREATE TABLE IF NOT EXISTS configuration(id integer PRIMARY KEY, subtitle text NOT NULL, information text NOT NULL);"
    connection.execute(sql)


def createConnection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
    except Exception as e:
        print(e)
    return conn


def prepareDataBase(nameOfBase):
    conn = createConnection(nameOfBase)
    createDataBase(conn)
    conn.close()


def writeInformationIntoBase(nameOfBase, subtitle, information):
    connection = createConnection(nameOfBase)
    sql = "INSERT INTO configuration('subtitle', 'information') VALUES('{}', '{}')".format(subtitle, information)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()


def getInformation(nameOfBase):
    connection = createConnection(nameOfBase)
    sql = "SELECT subtitle, information FROM configuration;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def printInformationFromBase(rows):
    text = ""
    for row in rows:
        text += "<fieldset>" + "<h3>"
        for words in row:
            text += str(words) + "<br>"
        text += "</h3>" + "</fieldset>" + "<br>"
    return text