#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

header = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    
}


res = requests.get('https://coinmarketcap.com/currencies/ethereum/', headers = header)

#from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text,'lxml')
data = soup.select_one('.priceValue___11gHJ')

dollars = float(data.text[1:].replace(',',''))
print(dollars)


# In[ ]:




