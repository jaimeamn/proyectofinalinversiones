from flaskapp.data_access.SqliteConnection import dbConnection
from datetime import date
from datetime import datetime

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

def saveMovement(movement):
    conn = dbConnection.getConnection()
    cursor = conn.cursor()
    query = ('INSERT INTO movimientos(fecha,hora,moneda_from,cantidad_from,moneda_to,cantidad_to) '
         'VALUES (:fecha, :hora, :moneda_to, :cantidad_to, :moneda_from, :cantidad_from);')
    
    completeDate = str(datetime.now())
    date = completeDate.split(" ")[0]
    hour = completeDate.split(" ")[1]
    
    params = {
            'fecha': date,
            'hora': hour.split(".")[0],
            'moneda_from': movement["moneda_from"],
            'cantidad_from': movement["cantidad_from"],
            'moneda_to': movement["moneda_to"],
            'cantidad_to': movement["cantidad_to"]
        }
    cursor.execute(query, params)
    conn.commit()
    conn.close()





