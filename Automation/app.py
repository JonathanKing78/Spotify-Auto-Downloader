import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/callback")
def start():
    return "Hello World"

app.run(debug=True)