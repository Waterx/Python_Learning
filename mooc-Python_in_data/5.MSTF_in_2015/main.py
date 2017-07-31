
# -*- coding: utf-8 -*-

import requests
import re
import pandas as pd
import json
from datetime import date
quotes = []
url = 'https://finance.yahoo.com/quote/MSFT/history?period1=1420041600&period2=1451577600&interval=1d&filter=history&frequency=1d'
r = requests.get(url)
m = re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"', r.text)
if m:
    quotes = json.loads(m[0])
    quotes = quotes[::-1]
quotes = [item for item in quotes if 'type' not in item]

for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    quotes[i]['date'] = date.strftime(x, '%Y-%m-%d')
    quotes[i]['month'] = date.strftime(x, '%m')

quotesdf = pd.DataFrame(quotes)
x = quotesdf.groupby('month').close.mean()
print(x)

