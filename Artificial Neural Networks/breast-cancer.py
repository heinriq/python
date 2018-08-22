# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:38:44 2017

@author: Jones
"""
import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPClassifier

base = datasets.load_breast_cancer()

neuralNetwork = MLPClassifier(
    verbose=True, 
    max_iter=1000,
    activation='logistic', 
    learning_rate_init=0.001
)
neuralNetwork.fit(base.data, base.target)
print(neuralNetwork.predict(np.array([base.data[0]])))
print(neuralNetwork.predict(np.array([base.data[20]])))
