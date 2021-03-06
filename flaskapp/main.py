import re
from urllib import response
import flask;

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

@app.route("/api/v1/movimiento", methods=['POST'])

def saveMovement():
    data = request.get_json()
    movement = data["data"]
    response = operation.saveMovement(movement)

    messageValidation = {
        "status": "success",
        "id": response[0],
        "monedas":  [response[3], response[5]]
    }
    return jsonify(messageValidation)

@app.route("/api/v1/tipo_cambio", methods=['GET'])

def getExchangeType():
    currencyFrom = request.args.get("moneda_from")
    currencyTo = request.args.get("moneda_to")
    quantityFrom = request.args.get("cantidad_from")

    #print({currencyFrom, currencyTo, quantityFrom})
    resultExchange = coin_api_conection.getExchange(currencyFrom, currencyTo)

    rate = resultExchange["rate"]
    quantityTo = (int(quantityFrom) * float(rate))
    message = {
        "status": "success",
        "data": {"tipo_cambio": "Precio unitario de " + currencyTo + "en valor de " + currencyFrom, 
        "unit_price": rate, 
        "quantityTo":quantityTo
        
        }     
    }

    # response = flask.make_response(message)
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Access-Control-Allow-Credentials'] = 'true'
         
    return jsonify(message)


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


@app.route("/api/v1/status", methods=['GET'])

def getInversionStatus():
     results = operation.currentValueCripto()
     print(results)
     theCriptoToEuro = 0
     for currency in results.keys():
         response = coin_api_conection.getExchange(currency, "EUR")
         rate = response["rate"]
         quantityEur = (int(results[currency]) * float(rate))
         theCriptoToEuro += quantityEur
     totalEur = operation.getTotalEur()    
     currentValue =  totalEur + operation.getBalanceEurosInvested() + theCriptoToEuro
     message = {
        "status": "success",
        "data": {"invertido": totalEur, 
        "valor_actual": currentValue
        
        }     
    }
         
     return jsonify(message)






     
  



    

    










