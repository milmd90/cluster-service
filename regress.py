import os
from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor

CLUSTERER_FILE_NAME = "clusterer.joblib"
MODEL_PATH = "models"
REGRESSOR_FILE_NAME = "regressor.joblib"

def regress(X, y):
    regressor = RandomForestRegressor(n_estimators=100, oob_score=True).fit(X, y)
    with open(os.path.join(MODEL_PATH, REGRESSOR_FILE_NAME), 'wb') as model_file:
        dump(regressor, model_file)