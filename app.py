from flask import Flask, render_template
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

    movies = []
    
    for row in rows:
        id = row[0]
        name = row[1]
        year = row[2]
        movies.append(f"{id} movie {name} {year}")
    
    print(movies)



    return render_template('index.html', items=movies)