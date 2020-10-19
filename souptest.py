#%%
import requests
import re
from bs4 import BeautifulSoup

url = 'http://military.people.com.cn/GB/1077/index.html'
res = requests.get(url)
html = res.text


soup = BeautifulSoup(html, "lxml")
print(res)

# %%
