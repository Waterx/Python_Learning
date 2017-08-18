# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:05:51 2017

@author: Ha
"""

# 利用 KNN 分类算法进行分类
import numpy as np
from sklearn import neighbors, datasets

n_neighbors = 3

iris = datasets.load_iris()
X = iris.data
y = iris.target
clf = neighbors.KNeighborsClassifier()
clf.fit(X, y)
print(clf.predict([[5.,3.,5.,2.]]))