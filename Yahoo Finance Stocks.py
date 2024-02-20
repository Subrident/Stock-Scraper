#!/usr/bin/env python
# coding: utf-8

# In[47]:


import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

gpu = input('What is the ticker symbol for your stock? ')

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; \ Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \ Chrome/84.0.4147.105 Safari/537.36'}
url = f'https://finance.yahoo.com/quote/{gpu}'


# In[48]:


result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

title = soup.find('h1', {'class': 'D(ib) Fz(18px)'})
streamer = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
sub_streamer = soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'})
pe_ratio = soup.find('td', {'data-test': 'PE_RATIO-value'})
target_est = soup.find('td', {'data-test': 'ONE_YEAR_TARGET_PRICE-value'})

title = title.string
price = streamer.string
percent_change = sub_streamer.string
pe_ratio = pe_ratio.string
target_est = target_est.string
print(title)
print(price)
print(percent_change)
print(pe_ratio)
print(target_est)


# In[51]:


print('Here are the up-to-date statistics for your stock!')
print('Title: ', title)
print('Current Price: ', price)
print('Percent Change: ', percent_change)
print('PE Ratio (TTM): ', pe_ratio)
print('1y Target Est: ', target_est)


# In[ ]:




