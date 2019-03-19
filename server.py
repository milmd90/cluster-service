from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask("cluster-service")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def hello():
    return "Hello world!"

@app.route("/recommend/<saleCode>")
@cross_origin()
def recommend(saleCode):
    return "Hello %s!" % saleCode
