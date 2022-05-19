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

import pickle


model_path = 'outcomes/trained_model.pkl'

with open(model_path, 'rb') as f:
    model = pickle.load(f)

print(model.predict([[0.0, 0.0, 1.0, 44.0, 72000.0]]))
