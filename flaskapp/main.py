from ast import Return
from flask import Flask
from flaskapp.data_access import operation

app = Flask(__name__, instance_relative_config=True)
app.app_context().push()

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

@app.route("/api/v1/movimientos", methods=['GET'])
def getMovements():
    movements = operation.getAllMovements()
    print(movements)
    return movements



#@app.teardown_appcontext
#def closedb():
#   SqliteConnection.close_connection()

if __name__ == '__main__':
    app.run(debug=True)






