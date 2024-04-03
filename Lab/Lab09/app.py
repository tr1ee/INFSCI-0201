import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)

@app.route("/")
def index():
    data = get_db()
    return render_template("poems.html", poems = data)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('poems.db')
        cursor = db.cursor()
        cursor.execute("SELECT title, author, text FROM poems")
        all_data = cursor.fetchall()
        all_data = [str(val[0] for val in all_data)]
    return cursor.fetchall()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()