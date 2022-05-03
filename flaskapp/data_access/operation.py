from ast import Param
from flaskapp.data_access.SqliteConnection import dbConnection
from datetime import date
from datetime import datetime
from flaskapp.data_access import *

def getAllMovements():
    conn = dbConnection.getConnection()
    cursor = conn.cursor()
    cursor.execute(GET_ALL_MOVEMENTS_QUERY)
    list = _cursorToDictionary(cursor)
    
    return list

def _cursorToDictionary(cursor):
    list = []
    for row in cursor: 
        movement = {}
        movement["id"] = row[COLUMN_ID]
        movement["fecha"] = row[COLUMN_FECHA]
        movement["hora"] = row[COLUMN_HORA]
        movement["moneda_from"] = row[COLUMN_CANTIDAD_FROM]
        movement["cantidad_from"] = row[COLUMN_CANTIDAD_FROM]
        movement["moneda_to"] = row[COLUMN_MONEDA_TO]
        movement["cantidad_to"] = row[COLUMN_CANTIDAD_TO]
        list.append(movement)
        
    return list

def saveMovement(movement):
    conn = dbConnection.getConnection()
    cursor = conn.cursor()
    query = (SAVE_MOVEMENT_QUERY)
    
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
    movement = getCreatedMovement(params)
    conn.close()
    return movement

def getCreatedMovement(params):
    conn = dbConnection.getConnection()
    cursor = conn.cursor()
    query = (CREATED_MOVEMENT_QUERY)
    cursor.execute(query, (params["fecha"], params["hora"], params["moneda_from"], params["cantidad_from"], params["moneda_to"], params["cantidad_to"]))
    movement = cursor.fetchone()
    return movement

def getBalanceEurosInvested():
    conn = dbConnection.getConnection()
    cursor = conn.cursor()
    query = (GET_BALANCE_EUROS_INVESTED)
    cursor.execute(query,("EUR", "EUR"))
    balance = cursor.fetchone()
    return balance 

def currentValueCriptoToEuro():
    conn = dbConnection.getConnection()
    cursor = conn.cursor()
    query = (CURRENT_VALUE_CRIPTO_TO_EURO)
    currencyValueResult = {}
    for currency in CURRENCIES:
        cursor.execute(query,(currency,currency))
        currencyValueResult[currency] = cursor.fetchone()

    return currencyValueResult
    
        



"""
Valor actual en euros de nuestras criptos: Al existir varias posibles criptos debemos 
• Para cada cripto obtener su total como: La suma de Cantidad_to de todos los 
movimientos cuya Moneda_to es la cripto en cuestión menos la suma de 
Cantidad_from de todos los movimientos cuya Moneda_from es la cripto en 
cuestión
"""

    





