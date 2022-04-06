from flaskapp.data_access.SqliteConnection import dbConnection

def getAllMovements():
    conn = dbConnection.getConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movimientos')
    list = cursorToDictionary(cursor)
    return list

def cursorToDictionary(cursor):
    list = []
    for row in cursor: 
        movement = {}
        movement["id"] = row[0]
        movement["fecha"] = row[1]
        movement["hora"] = row[2]
        movement["moneda_from"] = row[3]
        movement["cantidad_from"] = row[4]
        movement["moneda_to"] = row[5]
        movement["cantidad_to"] = row[6]
        list.append(movement)

        return list


