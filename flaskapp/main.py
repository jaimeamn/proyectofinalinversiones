from flask_cors import CORS
from flask import Flask, jsonify
from flaskapp.data_access import operation




app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.app_context().push()

@app.route("/api/v1/movimientos", methods=['GET'])
def getMovements():
     status = ""
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


#@app.teardown_appcontext
#def closedb():
#   SqliteConnection.close_connection()

if __name__ == '__main__':
    app.run(debug=True)






