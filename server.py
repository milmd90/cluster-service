import os
from joblib import load
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from learn.regress import REGRESSOR_FILE_NAME, MODEL_PATH
from learn.cluster import DATA_PATH, open_file, DEMO_FILE_NAME, DATA_PATH, ENCODER_FILE_NAME, process_data
from learn.predict_demo_clusters import predict_demo_clusters
from demo import DEMO_CLUSTER_1, DEMO_CLUSTER_2, DEMO_CLUSTER_3

# Looker queries had to be done manually, so csv files 
# mimic the response of the looker API

CLUSTER_1_FILE = "cluster_1.csv"
CLUSTER_2_FILE = "cluster_2.csv"
CLUSTER_3_FILE = "cluster_3.csv"

app = Flask("cluster-service")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def hello():
    return "Hello world!"

@app.route("/recommend/<sale_code>")
@cross_origin()
def recommend(sale_code):
  predicted_cluster = magic(sale_code) 
  cluster_file = ""
  if predicted_cluster == DEMO_CLUSTER_1:
    cluster_file = CLUSTER_1_FILE
  elif predicted_cluster == DEMO_CLUSTER_2:
    cluster_file = CLUSTER_2_FILE
  elif predicted_cluster == DEMO_CLUSTER_3:
    cluster_file = CLUSTER_3_FILE
  else:
    return jsonify("Bad sale code")
  # leave out headers and get 12 rows
  data = open_file(os.path.join(DATA_PATH, cluster_file))[1:12]
  # build products
  products = [{
    "id": data[i][0],
    # img
    "brand": data[i][1],
    "name": data[i][2],
    "price": data[i][3] 
    } for i in range(len(data))]
  return jsonify({
    "products": products
  })
  

def magic(sale_code):
    # load demo data
    demo_data = load(os.path.join(DATA_PATH, DEMO_FILE_NAME))
    target_idx = 0
    for i in range(len(demo_data)):
      row = demo_data[i]
      if row[0] == sale_code:
        target_idx = i
        break
    predicted_cluster = predict_demo_clusters(target_idx)
    return predicted_cluster
