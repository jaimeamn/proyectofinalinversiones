from flask import Flask
from flaskapp import SqliteConnection

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")

cn = SqliteConnection.getConnection()


