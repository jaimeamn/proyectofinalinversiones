from email import message
from sqlite3 import Cursor
from unittest import result
from flask_cors import CORS
from flask import Flask, jsonify, request
from flaskapp.data_access import operation
from flaskapp.adapter import coin_api_conection


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
    response = operation.saveMovement(movement)
    messageValidation = {
        "status": "success",
        "id": response[0],
        "monedas":  [response [3], response[5]]
    }
    return jsonify(messageValidation)

@app.route("/api/v1/tipo_cambio", methods=['GET'])

def getExchangeType():
    currencyFrom = request.args.get("moneda_from")
    currencyTo = request.args.get("moneda_to")
    quantityFrom = request.args.get("cantidad_from")
    resultExchance = coin_api_conection.getExchange(currencyFrom, currencyTo)
    rate = resultExchance["rate"]
    quantityTo = (int(quantityFrom) * float(rate))
    message = {
        "status": "success",
        "data": {"tipo_cambio": "Precio unitario de la" + currencyTo + "en valor de" + currencyFrom, 
        "unit_price": rate, 
        "quantityTo":quantityTo
        
        }     
    }
    message.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(message)









     
  



    

    










