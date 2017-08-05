# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:58:02 2017

@author: Ha
"""

import numpy as np
from scipy.cluster.vq import vq,kmeans,whiten
import random
list = [[],[],[],[],[]]
for x in range(5):
    list[x] = [random.randrange(0, 101) for i in range(5)]
data = np.array(list)
whiten = whiten(data)
centroids, a = kmeans(whiten, 3)
result,_ = vq(whiten, centroids)
print(result)