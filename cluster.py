import numpy as np
import csv
import os
from sklearn.cluster import KMeans
from sklearn import preprocessing
from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor

DATA_PATH = "data"
MODEL_PATH = "models"
DATA_FILE_NAME = "sale_data.csv"
MODEL_FILE_NAME = "clusterer.joblib"
N_CLUSTERS = 15

def cluster():
    data = open_file(os.path.join(DATA_PATH, DATA_FILE_NAME))
    X = process_data(data)
    # quick (but probably terrible) clusterer for now
    clusterer = KMeans(n_clusters=N_CLUSTERS).fit(X)
    dump(clusterer, MODEL_FILE_NAME)
    with open(os.path.join(MODEL_PATH, MODEL_FILE_NAME), 'wb') as model_file:
        dump(clusterer, model_file)

def open_file(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        return data

def process_data(data):
    # leave out headers and sale code
    trunc_data = [data[i][1:] for i in range(1, len(data))]
    # separate int and str columns for encoding
    int_cols = []
    str_cols = []
    test_row = trunc_data[0]
    for j in range(len(test_row)):
        ele = test_row[j]
        if ele.isdigit():
            col = [int(trunc_data[i][j]) for i in range(len(trunc_data))]
            int_cols.append(col)
        else:
            col = [trunc_data[i][j] for i in range(len(trunc_data))]
            str_cols.append(col)
    encoded_str_cols = []
    encoder = preprocessing.LabelEncoder()
    for col in str_cols:
        encoded_str_col = encoder.fit_transform(col)
        encoded_str_cols.append(encoded_str_col)
    # join columns after encoding
    cols = []
    for col in int_cols:
        cols.append(col)
    for col in encoded_str_cols:
        cols.append(col)
    # transpose columns
    X = np.array(cols).T
    return X

if __name__ == '__main__':
    cluster()
