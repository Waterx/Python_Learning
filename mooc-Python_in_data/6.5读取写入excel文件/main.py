
"""
Created on Fri Aug 11 10:21:52 2017

@author: Ha
"""

import pandas as pd
df = pd.read_excel('a.xlsx')
df['Sum_score'] = df['Python']+df['Math']
df.to_excel('b.xlsx', sheet_name='scores')