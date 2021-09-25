# ==============================================================
# Author: Rodoflo Ferro
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ==============================================================

# -*- coding: utf-8 -*-
 
import pickle
from sklearn import svm

import os


def train_model(x, y, save_path=''):
    """Train a model and save it to a file.

    Parameters
    ----------
    x : array-like, shape (n_samples, n_features)
        Training data.
    y : array-like, shape (n_samples,)
        Target values.
    save_path : str
        Path to save the model.
    """

    classifier = svm.SVC(kernel='rbf')
    classifier.fit(x, y)

    pkl_filename = os.path.join(save_path, 'trained_model.pkl')
    with open(pkl_filename, 'wb') as f:
        pickle.dump(classifier, f)