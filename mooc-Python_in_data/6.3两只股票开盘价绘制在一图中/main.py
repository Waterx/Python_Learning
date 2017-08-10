# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 20:56:25 2017

@author: Ha
"""

import requests
import re
import json
import pandas as pd
from datetime import date
import time
import matplotlib.pyplot as plt
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]
 
def group_by_month_open(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    for i in range(len(quotes)):
        x = date.fromtimestamp(quotes[i]['date'])
        y = date.strftime(x,'%Y-%m-%d')
        quotes[i]['date'] = y
        quotes[i]['month'] = date.strftime(x, '%m')
    quotesdf_ori = pd.DataFrame(quotes)
    quotrsdf = quotesdf_ori.drop(['date'], axis=1)
    return quotrsdf.groupby('month').open.mean()
IBMdf = group_by_month_open('IBM')
Inteldf = group_by_month_open('INTC')
x1 = IBMdf.index
y1 = IBMdf.values
x2 = Inteldf.index
y2 = Inteldf.values
plt.subplot(211)
plt.plot(x1, y1, color='r', marker='o')
plt.subplot(212)
plt.plot(x2, y2, color='g', marker='o')

