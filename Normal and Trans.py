from sklearn import preprocessing
import numpy as np
import csv
import pandas as pd

#Normalizing

file1 = "x-nokoi.csv"
data = pd.read_csv(file1, delimiter=',', error_bad_lines=False, header=None)
data = data.as_matrix()
where_are_NaNs = np.isnan(data)
data[where_are_NaNs] = 0
data_normalized = preprocessing.normalize(data, norm='l2', axis=0, copy=True)
data_normalized_frame = pd.DataFrame(data_normalized)
data_normalized_frame.to_csv('x-nokoi_normalized.csv', sep=',', encoding='utf-8', header=None, index=False)

#transpose
data_file1 = "x-nokoi_normalized.csv"
data_file2 = "y-nokoi.csv"
data_x = pd.read_csv(data_file1, delimiter=',', error_bad_lines=False, header=None)
data_transpose = data_x.transpose()
data_y = pd.read_csv(data_file2, delimiter=',', error_bad_lines=False, header=None)
data_final = pd.concat([data_transpose, data_y], axis=1)
print(data_final.head(10))
data_final.to_csv('nokoi.csv', sep=',', encoding='utf-8', index=False, header=False)
