from flask import Flask

app = Flask("cluster-service")

@app.route("/")
def hello():
    return "Hello world!"