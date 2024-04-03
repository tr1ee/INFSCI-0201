from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/another-poem")
def another_poem():
    return render_template("greet.html")

if __name__ == "__main__":
    app.run(debug=True)

