from sqlite3 import Cursor
from flask_cors import CORS
from flask import Flask, jsonify, request
from flaskapp.data_access import operation


app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.app_context().push()

status = ""

@app.route("/api/v1/movimientos", methods=['GET'])

def getMovements():
     
     movements = operation.getAllMovements()
     if  len(movements) > 0:
         status = "success"
     response = handleResponse(movements, status)     
     return jsonify(response)


def handleResponse(body, status):
    json = {}
    if status != "success":
        json["status"] = status
        json["message"] = "error en servicio"
    
    else:
        json ["status"] = status
        json["data"] = body
    
    return json

if __name__ == '__main__':
    app.run(debug=True)
#@app.teardown_appcontext
#def closedb():
#   SqliteConnection.close_connection()


@app.route("/api/v1/movimiento", methods=['POST'])

def saveMovement():
    data = request.get_json()
    movement = data["data"]
    operation.saveMovement(movement)
    return "gurdado con exito"
    










