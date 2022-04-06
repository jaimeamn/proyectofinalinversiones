import os  #permite manejar variables de entorno y otras operaciones del sistema 
import sqlite3
from flask import g #nos permite tenerel conetexto de la aplicacion

class dbConnection:

    def __init__(self) -> None:
        self.conn = self.getConnection()
        return self.conn

    def getConnection():
        pathdatabase = os.environ['PATH_DB']
        db = getattr(g, '_database', None)

        if db is None:
            db = g._database = sqlite3.connect(pathdatabase)
            print("conectado a")
        return db

    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()



