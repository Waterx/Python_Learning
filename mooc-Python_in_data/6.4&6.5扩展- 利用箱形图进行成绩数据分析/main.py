# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:58:20 2017

@author: Ha
"""

import numpy as np
import pandas as pd
df = pd.read_excel('score.xlsx')
df.boxplot()