# ==============================================================
# Author: Rodoflo Ferro
# Twitter: @rodo_ferro
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ==============================================================

# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


def impute_data(file_path, out_folder='', strategy='median'):
    """Impute missing values in the data.
    Writes the imputed data to a csv file.

    Parameters
    ----------
    file_path : str
        Path to the data file.
    """
    
    data = pd.read_csv(file_path)

    imputer = SimpleImputer(missing_values=np.nan, strategy=strategy)
    imputer = imputer.fit(data.iloc[:, 1:3])
    data.iloc[:, 1:3] = imputer.transform(data.iloc[:, 1:3])

    file_name = file_path.split('/')[-1]
    file_name = out_folder + file_name.split('.')[0]
    data.to_csv(file_name + '-imputed.csv', index=False)


def encode_data(file_path, out_folder=''):
    """Encode categorical data.
    Writes the encoded data to a csv file.

    Parameters
    ----------
    file_path : str
        Path to the data file.
    """

    data = pd.read_csv(file_path)

    label_encoder = LabelEncoder()
    data['LABEL_ENCODING'] = label_encoder.fit_transform(data.iloc[:, 0])
    data = data[['PAIS', 'LABEL_ENCODING', 'EDAD', 'SALARIO', 'COMPRA']]

    onehot_encoder = OneHotEncoder()
    onehot = onehot_encoder.fit_transform(data[['LABEL_ENCODING']]).toarray()
    data['ALEMANIA'] = onehot[:, 0]
    data['ESPANA'] = onehot[:, 1]
    data['FRANCIA'] = onehot[:, 2]
    data = data[[
        'PAIS', 'LABEL_ENCODING',
        'ALEMANIA', 'ESPANA', 'FRANCIA',
        'EDAD', 'SALARIO', 'COMPRA'
    ]]

    file_name = file_path.split('/')[-1].split('-')[0]
    file_name = out_folder + file_name.split('.')[0]
    data.to_csv(file_name + '-encoded.csv', index=False)


def load_data(file_path, x_labels, y_labels):
    """Load data from a csv file.

    Parameters
    ----------
    file_path : str
        Path to the data file.
    x_labels : list
        List of the features to be used as input.
    y_labels : list
        List of the labels to be used as output.
    """

    data = pd.read_csv(file_path)
    x = data[x_labels]
    y = data[y_labels]

    return x, y
