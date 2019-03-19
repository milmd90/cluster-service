from flask import Flask

app = Flask("cluster-service")

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/recommend/<saleCode>")
def recommend(saleCode):
    return "Hello %s!" % saleCode
