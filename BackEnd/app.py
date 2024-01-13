import flask
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hi")
def start():
    return "Hello World"

app.run(debug=True)