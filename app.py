from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/movies")
def movies():
    connection = sqlite3.connect("movies.db")

    cursor = connection.cursor()
    
    rows = cursor.execute("select id, name, year from movies").fetchall()
    print(rows)



    return "<p>This is a special psychological picture</p>"