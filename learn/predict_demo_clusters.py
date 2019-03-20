import os
from joblib import load
from regress import REGRESSOR_FILE_NAME, MODEL_PATH
from cluster import DEMO_FILE_NAME, DATA_PATH, process_data


def predict_demo_clusters():
    # load regressor and demo data
    regressor = load(os.path.join(MODEL_PATH, REGRESSOR_FILE_NAME))
    demo_data = load(os.path.join(DATA_PATH, DEMO_FILE_NAME))
    # process demo data
    trunc_data = [demo_data[i][1:] for i in range(len(demo_data))]
    X = process_data(trunc_data)
    # predict demo clusters
    y = regressor.predict(X)
    # print demo clusters
    for num in y:
        print(int(round(num, 0)))   