import flask

app = flask.Flask(__name__)

@app.route("/hi")
def start():
    return "Hello World"

app.run()