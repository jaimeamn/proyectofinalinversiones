from flaskapp.data_access.SqliteConnection import dbConnection

def getAllMovements():
    conn = dbConnection.getConnection()
    cursor = conn.cursor()
    movemenslist = cursor.execute("SELECT * FROM movimientos;")
    list = cursorToDictionary(movemenslist)
    return list

def cursorToDictionary(cursor):
    list = {}
    for row in cursor: 
        list["id"] = row[0]
        list["fecha"] = row[1]
        list["hora"] = row[2]
        list["moneda_from"] = row[3]
        list["cantidad_from"] = row[4]
        list["moneda_to"] = row[5]
        list["cantidad_to"] = row[6]

    return list

