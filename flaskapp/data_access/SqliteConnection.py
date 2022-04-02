from importlib.resources import path
import sqlite3
#from flask import g

pathdatabase = "/sqlite/inversiones.sqlite"

def getConnection():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = sqlite3.connect(pathdatabase)
        print("conectado a" + db)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
