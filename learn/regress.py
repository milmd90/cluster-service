import os
from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor
from .cluster import CLUSTERER_FILE_NAME

MODEL_PATH = "models"
REGRESSOR_FILE_NAME = "regressor.joblib"

def regress(X, y):
    regressor = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=0).fit(X, y)
    with open(os.path.join(MODEL_PATH, REGRESSOR_FILE_NAME), 'wb') as model_file:
        dump(regressor, model_file)