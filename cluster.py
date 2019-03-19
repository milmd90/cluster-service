from sklearn.cluster import MeanShift
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from sklearn import preprocessing
from sklearn import datasets
import numpy as np
import pandas as pd

sale_file = 'sale_data.csv'
sale_frame = pd.read_csv(sale_file)
int_cols = []
str_cols = []
for col_name in sale_frame:
    col = sale_frame[col_name]
    ele = col[0]
    if isinstance(ele, str):
        str_cols.append(col)
    else:
        int_cols.append(col)
encoder = preprocessing.LabelEncoder()
encoded_str_cols = []
for col in str_cols:
    encoded_str_col = encoder.fit_transform(col)
    encoded_str_cols.append(encoded_str_col)
print(len(int_cols))
print(len(encoded_str_cols))
# print(pd_file)
# clustering = MeanShift().fit(X)
# clustering = KMeans(n_clusters=3, random_state=0).fit(X)
# print(X)
# print(y)
# print("Test Element")
# print(test_sample)
# print("Labels")
# print(clustering.labels_)
# print("Predicted Label")
# print(clustering.predict([test_sample]))
# print("Correct Label")
# print(test_label)
