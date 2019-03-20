import os
import csv
import numpy as np
from joblib import dump, load
from sklearn import preprocessing
from sklearn.cluster import KMeans, MeanShift, AgglomerativeClustering

N_CLUSTERS = 100
DATA_PATH = "data"
DATA_FILE_NAME = "sale_data.csv"
DEMO_FILE_NAME = "demo.joblib"
CLUSTERER_PATH = "models"
CLUSTERER_FILE_NAME = "clusterer.joblib"
ENCODER_FILE_NAME = "encoder.joblib"
# rows for these will be removed from training data, and saved for demo cluster prediction
DEMO_SALE_CODES = [
    "ZZZQ2",
    "ZZXG3",
    "ZZEQD"
]

def cluster():
    data = open_file(os.path.join(DATA_PATH, DATA_FILE_NAME))
    # leave out headers and sale code (demo sales)
    demo_sales = [data[i] for i in range(1, len(data)) if data[i][0] in DEMO_SALE_CODES] 
    # leave out headers and sale code
    trunc_data = [data[i][1:] for i in range(1, len(data)) if not data[i][0] in DEMO_SALE_CODES]
    sale_codes = [data[i][0] for i in range(1, len(data)) if not data[i][0] in DEMO_SALE_CODES] 
    X = process_data(trunc_data)
    # create clusterer and save model
    clusterer = AgglomerativeClustering(n_clusters=N_CLUSTERS).fit(X)
    with open(os.path.join(CLUSTERER_PATH, CLUSTERER_FILE_NAME), 'wb') as model_file:
        dump(clusterer, model_file)
    # save demo sale data
    with open(os.path.join(DATA_PATH, DEMO_FILE_NAME), 'wb') as demo_file:
        dump(demo_sales, demo_file)
    return sale_codes, X, clusterer.labels_

def open_file(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        return data

def process_data(data):
    # separate int and str columns for encoding
    int_cols = []
    str_cols = []
    test_row = data[0]
    for j in range(len(test_row)):
        ele = test_row[j]
        if ele.isdigit():
            col = [int(data[i][j]) for i in range(len(data))]
            int_cols.append(col)
        else:
            col = [data[i][j] for i in range(len(data))]
            str_cols.append(col)
    encoded_str_cols = []
    encoder = preprocessing.LabelEncoder()
    for col in str_cols:
        encoded_str_col = encoder.fit_transform(col)
        encoded_str_cols.append(encoded_str_col)
    with open(os.path.join( DATA_PATH, ENCODER_FILE_NAME), 'wb') as encoder_file:
        dump(encoder, encoder_file)
    # join columns after encoding
    cols = []
    for col in int_cols:
        cols.append(col)
    for col in encoded_str_cols:
        cols.append(col)
    # transpose columns
    X = np.array(cols).T
    return X